import tkinter as tk

def create_ui(root):
    ui_components = {}
    
    # Save the root window in the ui_components dictionary
    ui_components['root'] = root

    # Algorithm Selection
    ui_components['algorithm_menu'] = tk.StringVar(root)
    ui_components['algorithm_menu'].set("Bubble Sort")  # Default value
    algorithms = [
        "Bubble Sort", "Selection Sort", "Insertion Sort",
        "Merge Sort", "Quick Sort", "Heap Sort",
        "Radix Sort", "Counting Sort",
        "Linear Search", "Binary Search"
    ]
    ui_components['algorithm_menu_widget'] = tk.OptionMenu(root, ui_components['algorithm_menu'], *algorithms)
    ui_components['algorithm_menu_widget'].grid(row=0, column=0, padx=10, pady=10)

    # Input Entry
    ui_components['input_entry'] = tk.Entry(root, width=50)
    ui_components['input_entry'].grid(row=1, column=0, padx=10, pady=10)

    # Start Button
    ui_components['start_button'] = tk.Button(root, text="Start Visualization")
    ui_components['start_button'].grid(row=2, column=0, padx=10, pady=10)

    # Color Customization
    ui_components['color_label'] = tk.Label(root, text="Found Color:")
    ui_components['color_label'].grid(row=3, column=0, padx=10, pady=5)
    ui_components['color_entry'] = tk.Entry(root, width=20)
    ui_components['color_entry'].grid(row=4, column=0, padx=10, pady=5)
    ui_components['color_entry'].insert(0, "red")

    ui_components['default_color_label'] = tk.Label(root, text="Default Color:")
    ui_components['default_color_label'].grid(row=5, column=0, padx=10, pady=5)
    ui_components['default_color_entry'] = tk.Entry(root, width=20)
    ui_components['default_color_entry'].grid(row=6, column=0, padx=10, pady=5)
    ui_components['default_color_entry'].insert(0, "blue")

    # Delay Customization
    ui_components['delay_label'] = tk.Label(root, text="Delay (ms):")
    ui_components['delay_label'].grid(row=7, column=0, padx=10, pady=5)
    ui_components['delay_entry'] = tk.Entry(root, width=10)
    ui_components['delay_entry'].grid(row=8, column=0, padx=10, pady=5)
    ui_components['delay_entry'].insert(0, "500")

    # Button to Apply Customizations
    ui_components['apply_button'] = tk.Button(root, text="Apply Customizations", command=lambda: apply_customizations(ui_components))
    ui_components['apply_button'].grid(row=9, column=0, padx=10, pady=10)

    return ui_components

def apply_customizations(ui_components):
    found_color = ui_components['color_entry'].get()
    default_color = ui_components['default_color_entry'].get()
    delay = int(ui_components['delay_entry'].get())
    
    # Update visualizer with new settings
    ui_components['visualizer'].set_colors(found_color, default_color)
    ui_components['visualizer'].set_delay(delay)
