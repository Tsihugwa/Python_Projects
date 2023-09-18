import os
import tkinter as tk
from tkinter import filedialog

class FileManager:
    def __init__(self, root):
        self.root = root
        self.current_directory = os.getcwd()

        # Create a label to display the current directory
        self.label = tk.Label(self.root, text=self.current_directory)
        self.label.pack()

        # Create a button to open a file
        self.open_button = tk.Button(self.root, text="Open", command=self.open_file)
        self.open_button.pack()

        # Create a button to go to the parent directory
        self.up_button = tk.Button(self.root, text="Up", command=self.go_up)
        self.up_button.pack()

    def open_file(self):
        # Open a file using a file dialog
        file_path = filedialog.askopenfilename(initialdir=self.current_directory)
        print(f"Opening file: {file_path}")

    def go_up(self):
        # Go to the parent directory
        self.current_directory = os.path.abspath(os.path.join(self.current_directory, os.pardir))
        self.label.config(text=self.current_directory)

# Create the root window
root = tk.Tk()

# Set the window title
root.title("File Manager")

# Create an instance of the FileManager class
fm = FileManager(root)

# Run the Tkinter event loop
root.mainloop()
