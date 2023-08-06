import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
showinfo()
root.bind("<Button>", lambda event: print(event))  # mouse presses behave normally
root.bind("<Key>", lambda event: print(event))  # key presses do not work if a pop-up has been shown
root.mainloop()
