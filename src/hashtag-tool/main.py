"""
Handles GUI app
"""
# Imports
import tkinter as tk
from tkinter.font import Font

# Hashtag converter


def convert(text_input):
    """
    Convert strings into working hashtag strings
    Ex: Str1, St r2,  sTR 3, -> #str1,#str2,#str3
    """
    # Format - Remove space, put into lowercase, and split by comma
    cache = text_input.replace(" ", "").lower().split(",") 
    # Convert
    result = "".join(f'#{txt}' for txt in cache if txt)
    # Return
    return result


# GUI ops

def gui_convert():
    """
    GUI operation to convert input entry
    """
    txt_input = input_entry.get()
    txt_output = convert(txt_input)
    output_entry.insert("1.0", txt_output)


def gui_copy():
    """
    GUI operation to copy the converted result
    """
    txt_output = output_entry.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(txt_output)


def gui_clear():
    """
    GUI operation to clear the input and ouput entries
    """
    input_entry.delete(0, tk.END)
    output_entry.delete("1.0", tk.END)


# GUI build
root = tk.Tk()
root.title("Hashtag Converter")

# GUI style
root.geometry("800x600")
font = Font(family="Arial", size=16)

# Widgets - input
label_input = tk.Label(root, text="Enter Your\n Hashtags Here:", font=font)
label_input.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="we")
input_entry = tk.Entry(root, font=font)
input_entry.grid(row=0, column=1, padx=5, pady=10, sticky="we")

# Widget - output
label_output = tk.Label(root, text="Converted\n Hashtags:", font=font)
label_output.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="we")
output_entry = tk.Text(root, wrap="word", height=4)
output_entry.grid(row=2, column=1, padx=5, pady=10, sticky="we")

# Buttons
button_convert = tk.Button(root, text="Convert", font=font, command=gui_convert)
button_convert.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")
button_clear = tk.Button(root, text="Clear", font=font, command=gui_clear)
button_clear.grid(row=3, column=0, padx=10, pady=10, sticky="we")
button_copy = tk.Button(root, text="Copy", font=font, command=gui_copy)
button_copy.grid(row=3, column=1, padx=10, pady=10, sticky="we")

# GUI adaptive style
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# GUI ops
root.mainloop()
