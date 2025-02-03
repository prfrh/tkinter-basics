import tkinter as tk

window = tk.Tk()
window.title('My first button')

button = tk.Button(
    window,
    text="Click me!",
    width=25,
    height=5,
    command=window.destroy,
    bg="blue",
    fg="orange",
)
button.pack()
window.mainloop()
