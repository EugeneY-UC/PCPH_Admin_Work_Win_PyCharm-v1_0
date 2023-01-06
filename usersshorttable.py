# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
import usersshort as usr
from tkinter.messagebox import showinfo


users_list = usr.UsersShort()

root = tk.Tk()

root.title("Admin Dashboard")
root.geometry("1024x768")
root.minsize(640, 480)

tree = ttk.Treeview(root, columns=usr.user_short_fields, show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="User#")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="PIN")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Node#")

for user in users_list.users:
    tree.insert('', 0, values=(str(user.id), str(user.pin).zfill(4), str(user.node)))


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = str(item['values'])
        # show a message
        showinfo(title='Information', message=','.join(record))


tree.bind('<<TreeviewSelect>>', item_selected)

tree.pack()

if __name__ == "__main__":
    root.mainloop()
