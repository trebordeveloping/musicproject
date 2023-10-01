import tkinter as tk
from tkinter import filedialog
import os

from audiofileconversion import (
    convert_m4a_to_mp3
)

files_window = False

def print_path():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text="Selected Folder Path: " + folder_path)

def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text="Selected Folder Path: " + folder_path)

        if files_window:
            delete_window(files_window)

        new_window = tk.Toplevel(root)
        new_window.title(os.path.basename(folder_path))
        
        for file in os.listdir(folder_path):
            if file.endswith(".m4a"):
                label = tk.Label(new_window, text=file)
                label.pack()

def delete_window(files_window):
    if files_window:
        root.winfo_children()[-1].destroy()
        files_window = False

def convert():

    if folder_label.cget("text")=="No folder chosen":
        return
    
    folder_path = folder_label.cget("text")[22:]
    try:
        convert_m4a_to_mp3(folder_path)
    except Exception as e:
        print(f"An error occured: {e}")
    
    new_window = tk.Toplevel(root)
    finished_label = tk.Label(new_window, text="Finished")
    finished_label.pack()

# root window
root = tk.Tk()
root.title("Music Project")
root.geometry("800x300")

# file conversion
fileconversion_label = "CONVERT FILES FROM M4A TO MP3"
fileconversion_label = tk.Label(root, text=fileconversion_label)
fileconversion_label.pack()

choosefolder_label = "Choose folder: "
choosefolder_label = tk.Label(root, text=choosefolder_label)
choosefolder_label.pack()

openfolder_button = tk.Button(root, text="Open Folder", command=print_path)
openfolder_button.pack(pady=20)

folder_label = "No folder chosen"
folder_label = tk.Label(root, text=folder_label)
folder_label.pack()

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=20)

# start main loop
root.mainloop()