# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import font as tk_font
from tkinter import ttk

import csv
import csvfiles
from powerlines import PowerLines, get_power_lines_header
from nodes import Nodes, get_nodes_header

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
    font_config_button = tk_font.Font(family='Helvetica',
                                      size=12,
                                      weight='bold')

    # noinspection SpellCheckingInspection
    label_header = tk.Label(frame_label,
                            text="Grizzl-E Power Hub Administration Tool",
                            font=font_header,
                            foreground='red',
                            background='cyan',
                            pady=4,
                            relief='solid')
    label_header.pack(expand=True, fill='both')

    font_control = tk_font.Font(family='Helvetica', size=18, weight='bold')

    button_powerline = tk.Button(frame_control,
                                 text="Power Lines",
                                 font=font_control,
                                 foreground='blue',
                                 background='light green',
                                 command=to_power_lines_frame)
    button_powerline.pack(expand=True, fill='both')
    button_powerline.configure(relief='sunken')

    button_nodes = tk.Button(frame_control,
                             text='Nodes',
                             font=font_control,
                             foreground='blue',
                             background='#90EE90',
                             command=to_nodes_frame)
    button_nodes.pack(expand=True, fill='both')

    button_customers = tk.Button(frame_control,
                                 text="Customers",
                                 font=font_control,
                                 foreground='blue',
                                 background='#90EE90',
                                 command=to_customers_frame)
    button_customers.pack(expand=True, fill='both')

    button_schedules = tk.Button(frame_control,
                                 text="Schedules",
                                 font=font_control,
                                 foreground='blue',
                                 background='#90EE90',
                                 command=to_schedules_frame)
    button_schedules.pack(expand=True, fill='both')

    button_reports = tk.Button(frame_control,
                               text="Reports",
                               font=font_control,
                               foreground='blue',
                               background='#90EE90',
                               command=to_reports_frame)
    button_reports.pack(expand=True, fill='both')

    button_owner = tk.Button(frame_control,
                             text="Owner Details",
                             font=font_control,
                             foreground='blue',
                             background='#90EE90',
                             command=to_owner_frame)
    button_owner.pack(expand=True, fill='both')

    frame_power_lines = tk.Frame(frame_config)
    frame_power_lines.pack(expand=True, fill='both', padx=12, pady=12)
    control_frame_num = 1

    frame_header_power_lines = tk.Frame(frame_power_lines,
                                        background='light green',
                                        relief='solid', border=1)
    frame_header_power_lines.pack(expand=False, fill='both', side='top')

    label_power_lines = tk.Label(frame_header_power_lines,
                                 background='light green',
                                 text='Power Lines',
                                 font=font_config_header)
    label_power_lines.pack()

    frame_footer_power_lines = tk.Frame(frame_power_lines,
                                        pady=18,
                                        background='light green',
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
                                  background='light green',
                                  relief='solid', border=1)
    frame_header_nodes.pack(expand=False, fill='both', side='top')

    label_nodes = tk.Label(frame_header_nodes,
                           background='light green',
                           text='Nodes (Charge Points)',
                           font=font_config_header)
    label_nodes.pack()

    frame_footer_nodes = tk.Frame(frame_nodes,
                                  pady=18,
                                  background='light green',
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

    nodes_table.heading(node_columns[0], text='#', anchor='c')
    nodes_table.heading(node_columns[1], text='ID#', anchor='c')
    nodes_table.heading(node_columns[2], text='Node Name', anchor='c')
    nodes_table.heading(node_columns[3], text='Address', anchor='c')
    nodes_table.heading(node_columns[4], text='Type', anchor='c')
    nodes_table.heading(node_columns[5], text='Status', anchor='c')
    nodes_table.heading(node_columns[6], text='Power Line ID#', anchor='c')

    nodes_table.column('#1', stretch='no', width=20, anchor='c')
    nodes_table.column('#2', stretch='no', width=30, anchor='c')
    nodes_table.column('#3', width=55, anchor='c')
    nodes_table.column('#5', stretch='no', width=55)
    nodes_table.column('#6', stretch='no', width=55)
    nodes_table.column('#7', stretch='no', width=80, anchor='c')

    all_nodes = nodes.get_all_to_show_in_table()
    for node in all_nodes:
        nodes_table.insert('', 'end', values=node)

    frame_customers = tk.Frame(frame_config)

    frame_header_customers = tk.Frame(frame_customers,
                                      background='light green',
                                      relief='solid',
                                      border=1)
    frame_header_customers.pack(expand=False, fill='both', side='top')

    label_customers = tk.Label(frame_header_customers,
                               background='light green',
                               text='Customers',
                               font=font_config_header)
    label_customers.pack()

    frame_footer_customers = tk.Frame(frame_customers,
                                      pady=18,
                                      background='light green',
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

    frame_schedules = tk.Frame(frame_config)

    frame_header_schedules = tk.Frame(frame_schedules,
                                      background='light green',
                                      relief='solid',
                                      border=1)
    frame_header_schedules.pack(expand=False, fill='both', side='top')

    label_schedules = tk.Label(frame_header_schedules,
                               background='light green',
                               text='Schedules',
                               font=font_config_header)
    label_schedules.pack()

    frame_footer_schedules = tk.Frame(frame_schedules,
                                      pady=18,
                                      background='light green',
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
                                    background='light green',
                                    relief='solid',
                                    border=1)
    frame_header_reports.pack(expand=False, fill='both', side='top')

    label_reports = tk.Label(frame_header_reports,
                             background='light green',
                             text='Reports',
                             font=font_config_header)
    label_reports.pack()

    frame_footer_reports = tk.Frame(frame_reports,
                                    pady=18,
                                    background='light green',
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
                                  background='light green',
                                  relief='solid',
                                  border=1)
    frame_header_owner.pack(expand=False, fill='both', side='top')

    label_owner = tk.Label(frame_header_owner,
                           background='light green',
                           text='Owner Details',
                           font=font_config_header)
    label_owner.pack()

    frame_footer_owner = tk.Frame(frame_owner,
                                  pady=18,
                                  background='light green',
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
