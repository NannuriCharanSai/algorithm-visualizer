import tkinter as tk
from ui import create_ui
from visualizer import Visualizer

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Algorithm Visualizer")
    root.geometry("800x600")
    
    # Create UI components
    ui_components = create_ui(root)
    
    # Initialize the visualizer with the UI components
    visualizer = Visualizer(ui_components)
    ui_components['visualizer'] = visualizer  # Ensure visualizer is accessible for customization
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
