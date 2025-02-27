import tkinter as tk

def greet():
    print("Hello, welcome to the app!")

root = tk.Tk()
button = tk.Button(root, text="Greet", command=greet)
button.pack()
root.mainloop()