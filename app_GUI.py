import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Plant Care")
root.geometry("600x850")

label = ttk.Label(root, text = "Welcome to my little Plant Care app", font =("times new roman", 24))
label.pack (pady=50)
# main content frame (pack it so it's visible)
content = ttk.Frame(root, padding=10)
content.pack(fill='both', expand=True)

# a button inside the content frame (also packed)
button = ttk.Button(root, text="Done!", command=lambda: print(f"Button pressed!"))
button.pack(pady=20)

tk.
root.mainloop()