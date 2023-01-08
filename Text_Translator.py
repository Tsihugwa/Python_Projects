import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate():
    text = text_input.get()
    src = src_lang.get()
    dest = dest_lang.get()
    translator = Translator()
    translation = translator.translate(text, src=src, dest=dest)
    translation_output.set(translation.text)

# Create the main window
window = tk.Tk()
window.title("Translation Tool")

# Add a label for the text input
text_input_label = tk.Label(master=window, text="Enter text to translate:")
text_input_label.pack()

# Add a text input field
text_input = tk.Entry(master=window)
text_input.pack()

# Add a label for the source language
src_lang_label = tk.Label(master=window, text="Enter the source language code:")
src_lang_label.pack()

# Add a text input field for the source language
src_lang = tk.Entry(master=window)
src_lang.pack()

# Add a label for the destination language
dest_lang_label = tk.Label(master=window, text="Enter the destination language code:")
dest_lang_label.pack()

# Add a text input field for the destination language
dest_lang = tk.Entry(master=window)
dest_lang.pack()

# Add a translate button
translate_button = tk.Button(master=window, text="Translate", command=translate)
translate_button.pack()

# Add a label to display the translation
translation_output_label = tk.Label(master=window, text="Translation:")
translation_output_label.pack()

# Add a text field to display the translation
translation_output = tk.StringVar()
translation_output_field = tk.Entry(master=window, textvariable=translation_output, state="readonly")
translation_output_field.pack()

# Run the main loop
window.mainloop()
