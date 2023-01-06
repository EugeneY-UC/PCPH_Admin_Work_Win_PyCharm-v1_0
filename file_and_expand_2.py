import tkinter as tk

root = tk.Tk()
root.geometry('200x200+200+200')

tk.Label(root, text='Label', bg='green').pack(expand=True, fill=tk.Y)
tk.Label(root, text='Label2', bg='red').pack(expand=True, fill=tk.BOTH)

root.mainloop()
