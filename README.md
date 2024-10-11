# 📊 Real-Time Algorithm Visualizer 

Welcome to **Real-Time Algorithm Visualizer**, a Python-based application designed for visualizing various sorting and searching algorithms. Built with the Tkinter library, this tool offers an interactive way to observe the step-by-step execution of common algorithms with customizable visualization settings.

## 🚀 Features

- **Algorithm Visualization**: Supports popular algorithms, including:
  - Sorting: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, Radix Sort, Counting Sort
  - Searching: Linear Search, Binary Search
- **Customizable Colors**: Adjust the colors used to highlight found elements and default elements in the visualization.
- **Adjustable Speed**: Modify the delay between steps to control the speed of the visualization.
- **User-Friendly UI**: Built with Tkinter for a simple, interactive interface.
- **Modular Design**: The project is split into various Python files to keep the structure clean and manageable.

## 📂 Project Structure

- `main.py`: The entry point of the application. Initializes the Tkinter UI and connects all components.
- `algorithms.py`: Contains the sorting and searching algorithms used in the visualizations.
- `visualizer.py`: Handles the graphical representation and animations of algorithms.
- `config.py`: Configuration file to define customizable options like colors, delay, etc.

## 🛠 How to Run the Project

### Prerequisites

- Python 3.x
- Tkinter library (should come pre-installed with Python)
- Required libraries:
  ```bash
  pip install numpy pillow
  ```

### Running the Application

1. Clone or download the repository.
2. Run `main.py`:
   ```bash
   python main.py
   ```

3. The main interface will open, where you can:
   - Choose an algorithm from the dropdown menu.
   - Input a comma-separated list of numbers.
   - Customize the colors for "Found" and "Default" elements.
   - Set the delay (in milliseconds) to control the speed of the visualization.

4. Click "Start Visualization" to see the selected algorithm in action!

## 🖼️ User Interface Walkthrough

- **Algorithm Selection**: Select the desired algorithm from the dropdown menu.
- **Input Entry**: Enter a comma-separated list of numbers for sorting or searching.
- **Start Button**: Click to begin the visualization.
- **Customization Options**:
  - **Found Color**: Color used to highlight the element when found.
  - **Default Color**: Color used for elements in their default state.
  - **Delay**: Time delay between each visualization step (in milliseconds).
  
### Example

- Input: `5,3,8,6,2`
- Algorithm: Quick Sort
- Delay: `500 ms`

This will visualize how the Quick Sort algorithm sorts the list step by step.

## 🔧 Customization Options

- **Color Settings**: Modify the color settings directly in the UI or via the `config.py` file.
- **Delay Settings**: Adjust the speed of the visualization by altering the delay in milliseconds.
  
## 🧠 How It Works

### Visualization Engine (Visualizer.py)
- Handles rendering and animations for the algorithms.
- Colors and delay values can be dynamically adjusted during the visualization.

### Algorithm Implementations (Algorithms.py)
- Sorting algorithms are implemented using standard techniques and visualized in real-time.
- Searching algorithms use a similar approach to highlight found elements.

### UI Customization (Main.py)
- The `Tkinter` interface allows easy selection of algorithms, input, and configuration of visual parameters.

## 📈 Future Enhancements

- Add more algorithms like Dijkstra’s Shortest Path, Floyd-Warshall, etc.
- Include real-time feedback for users as the algorithm progresses.
- Optimize performance for larger data sets.

## 🧑‍💻 Contributions

Feel free to contribute to this project! Open a PR with any improvements or new features.

