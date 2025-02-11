import tkinter as tk
window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10, 
    height=10,

)
label.pack()

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="orange",
)
button.pack()

#Retrieving text with .get()
#Deleting text with .delete()
#Inserting text with .insert()

entry = tk.Entry(fg="orange", bg="blue", width=50)

window.mainloop()
