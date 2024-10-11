import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from algorithms import (
    bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort,
    heap_sort, radix_sort, counting_sort,
    linear_search, binary_search
)
from helpers import parse_input

class Visualizer:
    def __init__(self, ui_components):
        self.ui = ui_components
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.ui['root'])
        self.canvas.get_tk_widget().grid(row=4, column=0, padx=10, pady=10)
        self.ui['start_button'].config(command=self.start_visualization)
        
        # Customization Options
        self.colors = {'found': 'red', 'default': 'blue'}
        self.delay = 500  # Delay in milliseconds

    def start_visualization(self):
        algorithm = self.ui['algorithm_menu'].get()
        user_input = self.ui['input_entry'].get()

        if algorithm in ["Linear Search", "Binary Search"]:
            array, target = parse_input(user_input, search=True)
            if algorithm == "Linear Search":
                generator = linear_search(array, target)
            elif algorithm == "Binary Search":
                generator = binary_search(array, target)
            self.run_visualization(generator, search=True)
        
        elif algorithm in ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Radix Sort", "Counting Sort"]:
            array = parse_input(user_input)
            if algorithm == "Bubble Sort":
                generator = bubble_sort(array)
            elif algorithm == "Selection Sort":
                generator = selection_sort(array)
            elif algorithm == "Insertion Sort":
                generator = insertion_sort(array)
            elif algorithm == "Merge Sort":
                generator = merge_sort(array)
            elif algorithm == "Quick Sort":
                generator = quick_sort(array, 0, len(array) - 1)
            elif algorithm == "Heap Sort":
                generator = heap_sort(array)
            elif algorithm == "Radix Sort":
                generator = radix_sort(array)
            elif algorithm == "Counting Sort":
                generator = counting_sort(array)
            self.run_visualization(generator, search=False)

    def run_visualization(self, generator, search=False):
        try:
            self.ax.clear()
            data = next(generator)
            if search:
                index, array = data
                colors = [self.colors['found'] if i == index else self.colors['default'] for i in range(len(array))]
                self.ax.bar(range(len(array)), array, color=colors)
            else:
                if isinstance(data, tuple):  # Data might be a tuple (index, array) for sorting
                    index, array = data
                    colors = [self.colors['found'] if i == index else self.colors['default'] for i in range(len(array))]
                    self.ax.bar(range(len(array)), array, color=colors)
                else:  # Data is a list for sorting
                    self.ax.bar(range(len(data)), data)
            self.canvas.draw()
            self.ui['root'].after(self.delay, self.run_visualization, generator, search)
        except StopIteration:
            pass

    def set_colors(self, found_color, default_color):
        self.colors['found'] = found_color
        self.colors['default'] = default_color

    def set_delay(self, delay):
        self.delay = delay
