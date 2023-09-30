import tkinter as tk
from tkinter import filedialog
import os

files_window = False

def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text="Selected Folder Path: " + folder_path)

        if files_window:
            delete_window(files_window)

        new_window = tk.Toplevel(root)
        new_window.title(os.path.basename(folder_path))
        
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                label = tk.Label(new_window, text=file)
                label.pack()

def delete_window(files_window):
    if files_window:
        root.winfo_children()[-1].destroy()
        files_window = False



# root window
root = tk.Tk()
root.title("Music Project")
root.geometry("800x300")

# chose folder button
open_button = tk.Button(root, text="Open Folder", command=open_folder_dialog)
open_button.pack(pady=20)

folder_label = tk.Label(root, text="Choose a folder")
folder_label.pack()


# start main loop
root.mainloop()