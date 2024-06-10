# %%
"""
Handles GUI
"""
# Import
import tkinter as tk
from tkinter.font import Font
import converter 

# GUI function


def gui_convert():
    """
    GUI operation to convert input entry
    """
    txt_input = input_entry.get()
    txt_output = converter.convert(txt_input)
    label_output.config(text=txt_output)


def gui_copy():
    """
    GUI operation to copy the converted result
    """
    txt_output = label_output.cget("text")
    root.clipboard_clear()
    root.clipboard_append(txt_output)


def gui_clear():
    """
    GUI operation to clear the input entry
    """
    input_entry.delete(0, tk.END)


# GUI build
root = tk.Tk()
root.title("Hashtag Converter")

# GUI style
font = Font(family="Arial", size=12)

# Widgets - input
label_input = tk.Label(root, text="Enter your hashtags here:")
label_input.grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Buttons
button_convert = tk.Button(root, text="Convert", command=gui_convert)
button_convert.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
button_copy = tk.Button(root, text="Copy", command=gui_copy)
button_copy.grid(row=3, column=0, padx=5, pady=5)
button_clear = tk.Button(root, text="Clear", font=font, command=gui_clear)
button_clear.grid(row=3, column=1, padx=5, pady=5)

# Widget - output
label_output = tk.Label(root, text="")
label_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# GUI ops
root.mainloop()
