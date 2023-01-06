# -*- coding: utf-8 -*-

import csv
import powerlines
from csvfiles import CSV_PATH, NODES_CSV

node_fields = ("ID", "Charger Node Name", "Charger Node Address",
               "Charger Node Type", "Charger Node Status", "Power Line",
               "Record Status")
node_fields_to_show = 0, 1, 2, 3, 4, 5


def get_nodes_header():
    to_show = list()
    to_show.append('#')
    for column_num in node_fields_to_show:
        to_show.append(node_fields[column_num])
    return to_show


node_access_types = "PRIVATE", "PUBLIC", "MIXED"
node_statuses = "OFF", "ACTIVE", "REPAIR"


class Node:
    def __init__(self, node_id=0):
        self.__id = node_id
        self.__name = ''
        self.__address = ''
        self.__node_access = 0
        self.__power_line_id = 0
        self.__power_line = None
        self.__status = 0
        self.__record_status = False

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def node_type(self):
        return self.__node_access

    @node_type.setter
    def node_type(self, node_type):
        self.__node_access = node_type

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def power_line_id(self):
        return self.__power_line_id

    @power_line_id.setter
    def power_line_id(self, power_line_id):
        self.__power_line_id = power_line_id

    @property
    def power_line(self):
        return self.__power_line

    @power_line.setter
    def power_line(self, power_line):
        self.__power_line = power_line

    @property
    def record_status(self):
        return self.__record_status

    @record_status.setter
    def record_status(self, record_status):
        self.__record_status = record_status

    def get_node_to_show_in_table(self):
        to_show = list()
        to_show.append(self.__id)
        for column_num in node_fields_to_show:
            if column_num == 0:
                to_show.append(str(self.__id))
            if column_num == 1:
                to_show.append(self.__name)
            if column_num == 2:
                to_show.append(str(self.__address))
            if column_num == 3:
                to_show.append(node_access_types[self.__node_access])
            if column_num == 4:
                to_show.append(node_statuses[self.__status])
            if column_num == 5:
                to_show.append(str(self.__power_line_id))
        return to_show

    def __eq__(self, other):
        return self.__id == other.id \
               and self.__name == other.name \
               and self.__address == other.address \
               and self.__node_access == other.node_type \
               and self.__status == other.status \
               and self.__power_line == other.power_line \
               and self.__record_status == other.record_status

    def __str__(self):
        txt_power_line = 'None'
        if self.__power_line is not None:
            txt_power_line = self.__power_line.name
        field_0 = node_fields[0] + '# ' + str(self.__id)
        field_1 = node_fields[1] + ' -> ' + self.__name
        field_2 = node_fields[2] + ' -> ' + self.__address
        field_3 = '\n' + '\t' * 2 + node_fields[3] + ' -> '\
                  + node_access_types[self.__node_access]
        field_4 = ' ' + node_fields[4] + ' -> ' + node_statuses[self.__status]
        field_5 = node_fields[5] + ' ID# ' + ' -> ' + str(self.__power_line_id)
        field_5_link = node_fields[5] + ' -> ' + txt_power_line
        field_6 = '\n' + '\t' * 2 + node_fields[6] + ' -> '\
                  + str(self.__record_status)
        return ",\t".join([field_0, field_1, field_2, field_3, field_4,
                           field_5, field_5_link, field_6])


class Nodes:

    def __init__(self, power_line_connected=None, path=CSV_PATH + NODES_CSV):
        self.__nodes = self.__read_csv(power_line_connected, path)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, node_list):
        self.__nodes = node_list

    def get_all_to_show_in_table(self):
        res = list()
        num = 0
        for line in self.__nodes:
            line_text = line.get_node_to_show_in_table()
            if line.record_status:
                num += 1
                line_text[0] = str(num)
                res.append(line_text)
        return res

    def __eq__(self, other):
        res = len(self.__nodes) == len(other.nodes)
        if res:
            for count, line in enumerate(self.__nodes):
                res &= self.__nodes[count] == other.nodes[count]
        return res

    def __str__(self):
        nodes_str = ""
        for node in self.__nodes:
            nodes_str += '\n' + node.__str__()
        return nodes_str

    @staticmethod
    def __read_csv(power_lines_connected, path):
        read_nodes = list()
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_count = 0
            for row in csv_reader:
                column_count = 0
                for column in row:
                    if row_count == 0:
                        try:
                            if column != node_fields[column_count]:
                                msg = "CHECK COLUMN NAMES IN THE FILE -> %s"
                                raise Exception(msg % NODES_CSV)
                        except Exception as e:
                            print(e)
                    else:
                        if column_count == 0:           # ID
                            new_node = Node(int(column))
                        elif column_count == 1:         # Charger Node Name
                            new_node.name = column
                        elif column_count == 2:         # Charger Node Address
                            new_node.address = column
                        elif column_count == 3:         # Charger Node Type
                            i = 0
                            for node_type in node_access_types:
                                if column.upper() == node_type:
                                    break
                                i += 1
                            if i >= len(node_access_types):
                                i = 0
                            new_node.node_type = i
                        elif column_count == 4:         # Charger Node Status
                            i = 0
                            for node_status in node_statuses:
                                if column.upper() == node_status:
                                    break
                                i += 1
                            if i >= len(node_statuses):
                                i = 0
                            new_node.status = i
                        elif column_count == 5:         # Power Line
                            new_node.power_line_id = int(column)
                            if power_lines_connected is not None:
                                index = new_node.power_line_id - 1
                                new_node.power_line\
                                    = power_lines_connected[index]
                        elif column_count == 6:         # Power Line
                            new_node.record_status = column.upper() == 'ON'
                            read_nodes.append(new_node)
                    column_count += 1
                row_count += 1
        return read_nodes

    def save(self, path=CSV_PATH + "Test1\\" + NODES_CSV):
        self.__write_csv(path)

    def __write_csv(self, path):
        with open(path, mode='w') as write_file:
            csv_writer = csv.writer(write_file,
                                    delimiter=',',
                                    lineterminator='\n')
            csv_writer.writerow(node_fields)
            for node in self.__nodes:
                if node.record_status:
                    record_status_text = "ON"
                else:
                    record_status_text = "OFF"
                csv_writer.writerow([str(node.id), node.name, node.address,
                                    node_access_types[node.node_type],
                                    node_statuses[node.status],
                                    str(node.power_line_id),
                                    record_status_text])


if __name__ == "__main__":
    power_lines = powerlines.PowerLines()
    nodes = Nodes(power_lines)
    print(nodes)
    power_lines_test = powerlines.PowerLines(CSV_PATH + "Test\\"
                                             + "PowerLines.csv")
    nodes_test = Nodes(power_lines_test, CSV_PATH + "Test\\" + NODES_CSV)
    print(nodes_test)
    print(nodes == nodes_test)
    nodes_test.save()
    nodes_test1 = Nodes(power_lines_test, CSV_PATH + "Test1\\" + NODES_CSV)
    print(nodes_test1)
    print(nodes_test == nodes_test1)
