# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import font as tk_font
from tkinter import ttk

import csv
import csvfiles
from powerlines import PowerLines, get_power_lines_header
from nodes import Nodes, get_nodes_header
from users import Users, get_users_header

import os

for k, v in os.environ.items():
    print(f'{k}={v}')


def print_cvs(name):
    print(f'Hi, {name}')
    with open(csvfiles.CSV_PATH + csvfiles.POWER_LINES_CSV) as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are', {", ".join(row)})
            else:
                print(f'\t ID# {row[0]}, Line -> {row[1]},'
                      f'Max AMP -> {row[2]}, Active -> {row[3]}')
            line_count += 1
        print(f'Processed {line_count} lines')


control_frame_num = 0


# noinspection PyUnusedLocal
def start_space(event):
    global control_frame_num
    if control_frame_num == 0:
        to_power_lines_frame()


# noinspection PyUnusedLocal
def navigate_down(event):
    global control_frame_num
    if control_frame_num == 6:
        to_power_lines_frame()
        return
    if control_frame_num == 0:
        to_power_lines_frame()
        return
    if control_frame_num == 1:
        to_nodes_frame()
        return
    if control_frame_num == 2:
        to_customers_frame()
        return
    if control_frame_num == 3:
        to_schedules_frame()
        return
    if control_frame_num == 4:
        to_reports_frame()
        return
    if control_frame_num == 5:
        to_owner_frame()


# noinspection PyUnusedLocal
def navigate_up(event):
    global control_frame_num
    if control_frame_num == 1:
        to_owner_frame()
        return
    if control_frame_num == 0:
        to_owner_frame()
        return
    if control_frame_num == 2:
        to_power_lines_frame()
        return
    if control_frame_num == 3:
        to_nodes_frame()
        return
    if control_frame_num == 4:
        to_customers_frame()
        return
    if control_frame_num == 5:
        to_schedules_frame()
        return
    if control_frame_num == 6:
        to_reports_frame()


def to_power_lines_frame():
    global control_frame_num
    if control_frame_num == 2:
        frame_nodes.pack_forget()
        button_nodes.configure(relief='raised')
    if control_frame_num == 3:
        frame_customers.pack_forget()
        button_customers.configure(relief='raised')
    if control_frame_num == 4:
        frame_schedules.pack_forget()
        button_schedules.configure(relief='raised')
    if control_frame_num == 5:
        frame_reports.pack_forget()
        button_reports.configure(relief='raised')
    if control_frame_num == 6:
        frame_owner.pack_forget()
        button_owner.configure(relief='raised')
    control_frame_num = 1
    frame_power_lines.pack(expand=True, fill='both', padx=12, pady=12)
    button_powerline.configure(relief='sunken')


def to_nodes_frame():
    global control_frame_num
    if control_frame_num == 1:
        frame_power_lines.pack_forget()
        button_powerline.configure(relief='raised')
    if control_frame_num == 3:
        frame_customers.pack_forget()
        button_customers.configure(relief='raised')
    if control_frame_num == 4:
        frame_schedules.pack_forget()
        button_schedules.configure(relief='raised')
    if control_frame_num == 5:
        frame_reports.pack_forget()
        button_reports.configure(relief='raised')
    if control_frame_num == 6:
        frame_owner.pack_forget()
        button_owner.configure(relief='raised')
    control_frame_num = 2
    frame_nodes.pack(expand=True, fill='both', padx=12, pady=12)
    button_nodes.configure(relief='sunken')


def to_customers_frame():
    global control_frame_num
    if control_frame_num == 1:
        frame_power_lines.pack_forget()
        button_powerline.configure(relief='raised')
    if control_frame_num == 2:
        frame_nodes.pack_forget()
        button_nodes.configure(relief='raised')
    if control_frame_num == 4:
        frame_schedules.pack_forget()
        button_schedules.configure(relief='raised')
    if control_frame_num == 5:
        frame_reports.pack_forget()
        button_reports.configure(relief='raised')
    if control_frame_num == 6:
        frame_owner.pack_forget()
        button_owner.configure(relief='raised')
    control_frame_num = 3
    frame_customers.pack(expand=True, fill='both', padx=12, pady=12)
    button_customers.configure(relief='sunken')


def to_schedules_frame():
    global control_frame_num
    if control_frame_num == 1:
        frame_power_lines.pack_forget()
        button_powerline.configure(relief='raised')
    if control_frame_num == 2:
        frame_nodes.pack_forget()
        button_nodes.configure(relief='raised')
    if control_frame_num == 3:
        frame_customers.pack_forget()
        button_customers.configure(relief='raised')
    if control_frame_num == 5:
        frame_reports.pack_forget()
        button_reports.configure(relief='raised')
    if control_frame_num == 6:
        frame_owner.pack_forget()
        button_owner.configure(relief='raised')
    control_frame_num = 4
    frame_schedules.pack(expand=True, fill='both', padx=12, pady=12)
    button_schedules.configure(relief='sunken')


def to_reports_frame():
    global control_frame_num
    if control_frame_num == 1:
        frame_power_lines.pack_forget()
        button_powerline.configure(relief='raised')
    if control_frame_num == 2:
        frame_nodes.pack_forget()
        button_nodes.configure(relief='raised')
    if control_frame_num == 3:
        frame_customers.pack_forget()
        button_customers.configure(relief='raised')
    if control_frame_num == 4:
        frame_schedules.pack_forget()
        button_schedules.configure(relief='raised')
    if control_frame_num == 6:
        frame_owner.pack_forget()
        button_owner.configure(relief='raised')
    control_frame_num = 5
    frame_reports.pack(expand=True, fill='both', padx=12, pady=12)
    button_reports.configure(relief='sunken')


def to_owner_frame():
    global control_frame_num
    if control_frame_num == 1:
        frame_power_lines.pack_forget()
        button_powerline.configure(relief='raised')
    if control_frame_num == 2:
        frame_nodes.pack_forget()
        button_nodes.configure(relief='raised')
    if control_frame_num == 3:
        frame_customers.pack_forget()
        button_customers.configure(relief='raised')
    if control_frame_num == 4:
        frame_schedules.pack_forget()
        button_schedules.configure(relief='raised')
    if control_frame_num == 5:
        frame_reports.pack_forget()
        button_reports.configure(relief='raised')
    control_frame_num = 6
    frame_owner.pack(expand=True, fill='both', padx=12, pady=12)
    button_owner.configure(relief='sunken')


if __name__ == "__main__":
    print_cvs('PyCharm')
    power_lines = PowerLines()
    print(power_lines)
    nodes = Nodes(power_lines)
    print(nodes)
    users = Users(nodes)
    print(users)

    root = tk.Tk()
    # root.geometry('1280x720+275+225')
    root.geometry('1280x720')
    root.minsize(640, 480)

    root.bind('<space>', start_space)
    root.bind('<Down>', navigate_down)
    root.bind('<Up>', navigate_up)

    frame_label = tk.Frame(root)
    frame_label.pack(expand=False, fill='both', side='top')

    frame_control = tk.Frame(root)
    frame_control.pack(expand=False, fill='both', side='left')

    frame_config = tk.Frame(root, background='light gray')  # #ADD8E6
    frame_config.pack(expand=True, fill='both', side='right')

    font_header = tk_font.Font(family='Helvetica', size=24, weight='bold')
    font_config_header = tk_font.Font(family='Helvetica', size=20)

    # noinspection SpellCheckingInspection
    label_header = tk.Label(frame_label,
                            text="Grizzl-E Power Hub Administration Tool",
                            font=font_header,
                            foreground='red',
                            background='light cyan',
                            pady=4,
                            relief='solid')
    label_header.pack(expand=True, fill='both')

    font_control = tk_font.Font(family='Helvetica', size=18, weight='bold')

    button_powerline = tk.Button(frame_control,
                                 text="Power Lines",
                                 font=font_control,
                                 foreground='blue',
                                 background='#D8FFD8',
                                 command=to_power_lines_frame)
    button_powerline.pack(expand=True, fill='both')
    button_powerline.configure(relief='sunken')

    button_nodes = tk.Button(frame_control,
                             text='Nodes',
                             font=font_control,
                             foreground='blue',
                             background='lavender',
                             command=to_nodes_frame)
    button_nodes.pack(expand=True, fill='both')

    button_customers = tk.Button(frame_control,
                                 text="Customers",
                                 font=font_control,
                                 foreground='blue',
                                 background='#FFD8D8',
                                 command=to_customers_frame)
    button_customers.pack(expand=True, fill='both')

    button_schedules = tk.Button(frame_control,
                                 text="Schedules",
                                 font=font_control,
                                 foreground='blue',
                                 background='#FFFFD8',
                                 command=to_schedules_frame)
    button_schedules.pack(expand=True, fill='both')

    button_reports = tk.Button(frame_control,
                               text="Transactions",
                               font=font_control,
                               foreground='blue',
                               background='#FFD8FF',
                               command=to_reports_frame)
    button_reports.pack(expand=True, fill='both')

    button_owner = tk.Button(frame_control,
                             text="Owner Details",
                             font=font_control,
                             foreground='blue',
                             background='light cyan',
                             command=to_owner_frame)
    button_owner.pack(expand=True, fill='both')

    font_config_button\
        = tk_font.Font(family='Helvetica', size=12, weight='bold')

    frame_power_lines = tk.Frame(frame_config)
    frame_power_lines.pack(expand=True, fill='both', padx=12, pady=12)
    control_frame_num = 1

    frame_header_power_lines = tk.Frame(frame_power_lines,
                                        background='#D8FFD8',
                                        relief='solid', border=1)
    frame_header_power_lines.pack(expand=False, fill='both', side='top')

    label_power_lines = tk.Label(frame_header_power_lines,
                                 background='#D8FFD8',
                                 text='Power Lines',
                                 font=font_config_header)
    label_power_lines.pack()

    frame_footer_power_lines = tk.Frame(frame_power_lines,
                                        pady=18,
                                        background='#D8FFD8',
                                        relief='solid', border=1)
    frame_footer_power_lines.pack(expand=False, fill='both', side='bottom')

    button_power_lines_add = tk.Button(frame_footer_power_lines,
                                       width=8,
                                       background='light gray',
                                       font=font_config_button,
                                       text='Add New')
    button_power_lines_add.pack(side='left', expand=True)

    button_power_lines_edit = tk.Button(frame_footer_power_lines,
                                        width=8,
                                        background='light gray',
                                        font=font_config_button,
                                        text='Edit')
    button_power_lines_edit.pack(side='left', expand=True)

    button_power_lines_delete = tk.Button(frame_footer_power_lines,
                                          width=8,
                                          background='light gray',
                                          font=font_config_button,
                                          text='Delete')
    button_power_lines_delete.pack(side='right', expand=True)

    columns = get_power_lines_header()

    power_lines_table = ttk.Treeview(frame_power_lines,
                                     columns=columns,
                                     show="headings")
    power_lines_table.pack(fill='both', expand=True)

    power_lines_scrollbar = ttk.Scrollbar(power_lines_table,
                                          orient='vertical',
                                          command=power_lines_table.yview)
    power_lines_table.configure(yscroll=power_lines_scrollbar.set)
    power_lines_scrollbar.pack(fill='y', side='right')

    power_lines_table.heading(columns[0], text='#', anchor='c')
    power_lines_table.heading(columns[1], text='ID#', anchor='c')
    power_lines_table.heading(columns[2], text='Line Name', anchor='c')
    power_lines_table.heading(columns[3], text='Max AMP', anchor='c')
    power_lines_table.heading(columns[4], text='Active', anchor='c')

    power_lines_table.column('#1', stretch='no', width=20, anchor='c')
    power_lines_table.column('#2', stretch='no', width=30, anchor='c')
    power_lines_table.column('#4', width=50, anchor='c')
    power_lines_table.column('#5', stretch='no', width=75, anchor='c')

    all_lines = power_lines.get_all_to_show_in_table()
    for line in all_lines:
        power_lines_table.insert('', 'end', values=line)

    frame_nodes = tk.Frame(frame_config)

    frame_header_nodes = tk.Frame(frame_nodes,
                                  background='lavender',
                                  relief='solid', border=1)
    frame_header_nodes.pack(expand=False, fill='both', side='top')

    label_nodes = tk.Label(frame_header_nodes,
                           background='lavender',
                           text='Nodes (Charge Points)',
                           font=font_config_header)
    label_nodes.pack()

    frame_footer_nodes = tk.Frame(frame_nodes,
                                  pady=18,
                                  background='lavender',
                                  relief='solid',
                                  border=1)
    frame_footer_nodes.pack(expand=False, fill='both', side='bottom')

    button_nodes_add = tk.Button(frame_footer_nodes,
                                 width=8,
                                 background='light gray',
                                 font=font_config_button,
                                 text='Add New')
    button_nodes_add.pack(side='left', expand=True)

    button_nodes_edit = tk.Button(frame_footer_nodes,
                                  width=8,
                                  background='light gray',
                                  font=font_config_button,
                                  text='Edit')
    button_nodes_edit.pack(side='left', expand=True)

    button_nodes_schedule = tk.Button(frame_footer_nodes,
                                      width=8,
                                      background='light gray',
                                      font=font_config_button,
                                      text='Schedule')
    button_nodes_schedule.pack(side='left', expand=True)

    button_nodes_delete = tk.Button(frame_footer_nodes,
                                    width=8,
                                    background='light gray',
                                    font=font_config_button,
                                    text='Delete')
    button_nodes_delete.pack(side='right', expand=True)

    node_columns = get_nodes_header()

    nodes_table = ttk.Treeview(frame_nodes,
                               columns=node_columns,
                               show="headings")
    nodes_table.pack(fill='both', expand=True)

    nodes_scrollbar = ttk.Scrollbar(nodes_table,
                                    orient='vertical',
                                    command=nodes_table.yview)
    nodes_table.configure(yscroll=nodes_scrollbar.set)
    nodes_scrollbar.pack(fill='y', side='right')

    nodes_table.heading(node_columns[0], text='#', anchor='c')
    nodes_table.heading(node_columns[1], text='ID#', anchor='c')
    nodes_table.heading(node_columns[2], text='Node Name', anchor='c')
    nodes_table.heading(node_columns[3], text='Address', anchor='c')
    nodes_table.heading(node_columns[4], text='Type', anchor='c')
    nodes_table.heading(node_columns[5], text='Status', anchor='c')
    nodes_table.heading(node_columns[6], text='Power Line ID#', anchor='w')

    nodes_table.column('#1', stretch='no', width=20, anchor='c')
    nodes_table.column('#2', stretch='no', width=30, anchor='c')
    nodes_table.column('#3', width=55, minwidth=40, anchor='c')
    nodes_table.column('#5', stretch='no', width=55, anchor='c')
    nodes_table.column('#6', stretch='no', width=55, anchor='c')
    nodes_table.column('#7', stretch='no', width=100, anchor='c')

    all_nodes = nodes.get_all_to_show_in_table()
    for node in all_nodes:
        nodes_table.insert('', 'end', values=node)

    frame_customers = tk.Frame(frame_config)

    frame_header_customers = tk.Frame(frame_customers,
                                      background='#FFD8D8',
                                      relief='solid',
                                      border=1)
    frame_header_customers.pack(expand=False, fill='both', side='top')

    label_customers = tk.Label(frame_header_customers,
                               background='#FFD8D8',
                               text='Customers',
                               font=font_config_header)
    label_customers.pack()

    frame_footer_customers = tk.Frame(frame_customers,
                                      pady=18,
                                      background='#FFD8D8',
                                      relief='solid',
                                      border=1)
    frame_footer_customers.pack(expand=False, fill='both', side='bottom')

    button_customers_add = tk.Button(frame_footer_customers,
                                     width=8,
                                     background='light gray',
                                     font=font_config_button,
                                     text='Add New')
    button_customers_add.pack(side='left', expand=True)

    button_customers_edit = tk.Button(frame_footer_customers,
                                      width=8,
                                      background='light gray',
                                      font=font_config_button,
                                      text='Edit')
    button_customers_edit.pack(side='left', expand=True)

    button_nodes_delete = tk.Button(frame_footer_customers,
                                    width=8,
                                    background='light gray',
                                    font=font_config_button,
                                    text='Delete')
    button_nodes_delete.pack(side='right', expand=True)

    users_columns = get_users_header()

    users_table = ttk.Treeview(frame_customers,
                               columns=users_columns,
                               show="headings")
    users_table.pack(fill='both', expand=True)

    users_vertical_scrollbar = ttk.Scrollbar(users_table,
                                             orient='vertical',
                                             command=users_table.yview)
    users_table.configure(yscroll=users_vertical_scrollbar.set)
    users_vertical_scrollbar.pack(fill='y', side='right')

    users_horizontal_scrollbar = ttk.Scrollbar(users_table,
                                               orient='horizontal',
                                               command=users_table.xview)
    users_table.configure(xscroll=users_horizontal_scrollbar.set)
    users_horizontal_scrollbar.pack(fill='x', side='bottom')

    users_table.heading(users_columns[0], text='#')
    users_table.heading(users_columns[1], text='ID#')
    users_table.heading(users_columns[2], text='First Name')
    users_table.heading(users_columns[3], text='Second Name')
    users_table.heading(users_columns[4], text='Address')
    users_table.heading(users_columns[5], text='Phone')
    users_table.heading(users_columns[6], text='Email')
    users_table.heading(users_columns[7], text='User Name')
    users_table.heading(users_columns[8], text='Temp Pass')
    users_table.heading(users_columns[9], text='PIN')
    users_table.heading(users_columns[10], text='Active')
    users_table.heading(users_columns[11], text='Parking Slot')
    users_table.heading(users_columns[12], text='Node ID', anchor='w')

    users_table.column('#1', stretch='no', width=20, anchor='c')
    users_table.column('#2', stretch='no', width=30, anchor='c')
    users_table.column('#3', width=65, minwidth=65)
    users_table.column('#4', width=85, minwidth=85)
    users_table.column('#5', minwidth=205)
    users_table.column('#6', width=85, minwidth=85)
    users_table.column('#7', width=165, minwidth=125)
    users_table.column('#8', width=95, minwidth=75, anchor='c')
    users_table.column('#9', width=85, minwidth=65, anchor='c')
    users_table.column('#10', width=55, minwidth=45, anchor='c')
    users_table.column('#11', stretch='no', width=45, anchor='c')
    users_table.column('#12', width=75, minwidth=47, anchor='c')
    users_table.column('#13', stretch='no', width=65, anchor='c')

    all_users = users.get_all_to_show_in_table()
    for user in all_users:
        users_table.insert('', 'end', values=user)

    frame_schedules = tk.Frame(frame_config)

    frame_header_schedules = tk.Frame(frame_schedules,
                                      background='#FFFFD8',
                                      relief='solid',
                                      border=1)
    frame_header_schedules.pack(expand=False, fill='both', side='top')

    label_schedules = tk.Label(frame_header_schedules,
                               background='#FFFFD8',
                               text='Schedules',
                               font=font_config_header)
    label_schedules.pack()

    frame_footer_schedules = tk.Frame(frame_schedules,
                                      pady=18,
                                      background='#FFFFD8',
                                      relief='solid',
                                      border=1)
    frame_footer_schedules.pack(expand=False, fill='both', side='bottom')

    button_schedules_edit = tk.Button(frame_footer_schedules,
                                      width=8,
                                      background='light gray',
                                      font=font_config_button,
                                      text='Edit')
    button_schedules_edit.pack(side='left', expand=True)

    frame_reports = tk.Frame(frame_config)

    frame_header_reports = tk.Frame(frame_reports,
                                    background='#FFD8FF',
                                    relief='solid',
                                    border=1)
    frame_header_reports.pack(expand=False, fill='both', side='top')

    label_reports = tk.Label(frame_header_reports,
                             background='#FFD8FF',
                             text="Transactions and Reports",
                             font=font_config_header)
    label_reports.pack()

    frame_footer_reports = tk.Frame(frame_reports,
                                    pady=18,
                                    background='#FFD8FF',
                                    relief='solid',
                                    border=1)
    frame_footer_reports.pack(expand=False, fill='both', side='bottom')

    button_reports_edit = tk.Button(frame_footer_reports,
                                    width=8,
                                    background='light gray',
                                    font=font_config_button,
                                    text='Edit')
    button_reports_edit.pack(side='left', expand=True)

    frame_owner = tk.Frame(frame_config)

    frame_header_owner = tk.Frame(frame_owner,
                                  background='light cyan',
                                  relief='solid',
                                  border=1)
    frame_header_owner.pack(expand=False, fill='both', side='top')

    label_owner = tk.Label(frame_header_owner,
                           background='light cyan',
                           text='Owner Details',
                           font=font_config_header)
    label_owner.pack()

    frame_footer_owner = tk.Frame(frame_owner,
                                  pady=18,
                                  background='light cyan',
                                  relief='solid',
                                  border=1)
    frame_footer_owner.pack(expand=False, fill='both', side='bottom')

    button_owner_edit = tk.Button(frame_footer_owner,
                                  width=8,
                                  background='light gray',
                                  font=font_config_button,
                                  text='Edit')
    button_owner_edit.pack()

    root.mainloop()
