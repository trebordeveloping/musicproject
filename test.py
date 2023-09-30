import tkinter as tk

# Boolean variable to track whether a window exists
window_created = False

# Function to create a new window
def create_window():
    global window_created  # Access the global variable
    if not window_created:
        new_window = tk.Toplevel(root)
        new_window.title("New Window")
        new_window.geometry("300x200")
        new_window_label = tk.Label(new_window, text="This is a new window!")
        new_window_label.pack()
        window_created = True  # Set the variable to True after creating the window

# Function to delete the window if it exists
def delete_window():
    global window_created  # Access the global variable
    if window_created:
        root.winfo_children()[-1].destroy()  # Destroy the top window
        window_created = False  # Set the variable to False after deleting the window

# Create the main application window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

# Create a button to create a new window
create_button = tk.Button(root, text="Create Window", command=create_window)
create_button.pack(pady=20)

# Create a button to delete the window
delete_button = tk.Button(root, text="Delete Window", command=delete_window)
delete_button.pack()

# Start the main event loop
root.mainloop()
