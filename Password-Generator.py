
import tkinter.clipboard
from tkinter import ttk
import string
import random

# function to generate a strong password
def generate_password(length, special_chars, numbers):
    # create a string of all characters that can be used in the password
    password_characters = string.ascii_letters + string.digits
    if special_chars:
        password_characters += string.punctuation
    
    # create a list to store the password
    password = []
    
    # add a random special character to the password if required
    if special_chars:
        password.append(random.choice(string.punctuation))
    
    # add a random number to the password if required
    if numbers:
        password.append(random.choice(string.digits))
    
    # add random alphabets and digits to the password
    for i in range(length - len(password)):
        password.append(random.choice(password_characters))
    
    # shuffle the password to make it more unpredictable
    random.shuffle(password)
    
    # return the password as a string
    return ''.join(password)

# create the main window
root = tk.Tk()
root.title("Strong Password Generator")

# create the input fields
length_label = ttk.Label(root, text="Length:")
length_entry = ttk.Entry(root)
length_entry.insert(0, "8")

special_chars_label = ttk.Label(root, text="Include special characters:")
special_chars_checkbutton = ttk.Checkbutton(root)

numbers_label = ttk.Label(root, text="Include numbers:")
numbers_checkbutton = ttk.Checkbutton(root)

# create the generate button
generate_button = ttk.Button(root, text="Generate")

# create the output field
password_label = ttk.Label(root, text="Password:")
password_output = ttk.Label(root, text="")

#function to copy the password to the clipboard
def copy_password():
tkinter.clipboard.copy(password_output['text'])

copy_button = ttk.Button(root, text="Copy", command=copy_password)

#create a grid to add the widgets to
input_grid = tk.Frame(root)
input_grid.grid(column=0, row=0, sticky="W")

#add the input fields to the grid
length_label.grid(column=0, row=0, sticky="W")
length_entry.grid(column=1, row=0)

special_chars_label.grid(column=0, row=1, sticky="W")
special_chars_checkbutton.grid(column=1, row=1)

numbers_label.grid(column=0, row=2, sticky="W")
numbers_checkbutton.grid(column=1, row=2)

#add the generate button to the grid
generate_button.grid(column=0, row=3, columnspan=2)

#create a grid to add the output widgets to
output_grid = tk.Frame(root)
output_grid.grid(column=0, row=1, sticky="W")

#add the output widgets to the grid
password_label.grid(column=0, row=0, sticky="W")
password_output.grid(column=1, row=0)
copy_button.grid(column=2, row=0)

#create a function to generate a password when the generate button is clicked
def generate_password_click():
length = int(length_entry.get())
special_chars = special_chars_checkbutton.state() == ('selected',)
numbers = numbers_checkbutton.state() == ('selected',)

password = generate_password(length, special_chars, numbers)
password_output['text'] = password

#bind the generate button to the generate_password_click function
generate_button['command'] = generate_password_click

#run the main loop
root.mainloop()
