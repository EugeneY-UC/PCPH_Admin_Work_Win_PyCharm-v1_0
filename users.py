# -*- coding: utf-8 -*-

import csv
import powerlines as pl
import nodes
from csvfiles import CSV_PATH, USERS_CSV, NODES_CSV, POWER_LINES_CSV

user_fields = ("ID", "First Name", "Second Name", "Address", "Phone", "Email",
               "User Name", "Pass", "Pin", "User Status", "Parking Slot",
               "Node", "Record Status")
user_fields_to_show = range(12)


def get_users_header():
    to_show = list()
    to_show.append('#')
    for column_num in user_fields_to_show:
        to_show.append(user_fields[column_num])
    return to_show


class User:

    def __init__(self, user_id=0):
        self.__id = user_id
        self.__first_name = ''
        self.__second_name = ''
        self.__address = ''
        self.__phone = ''
        self.__email = ''
        self.__user_name = ''
        self.__password = ''
        self.__pin = ''
        self.__user_status = False
        self.__parking_slot_name = ''
        self.__node_id = 0
        self.__node = None
        self.__record_status = False

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def second_name(self):
        return self.__second_name

    @second_name.setter
    def second_name(self, second_name):
        self.__second_name = second_name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        self.__user_name = user_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    def pass_to_show(self):
        to_show = ""
        for _ in self.__password:
            to_show += '*'
        if len(to_show) <= 6:
            to_show = "******"
        return to_show

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def user_status(self):
        return self.__user_status

    @user_status.setter
    def user_status(self, user_status):
        self.__user_status = user_status

    @property
    def parking_slot(self):
        return self.__parking_slot_name

    @parking_slot.setter
    def parking_slot(self, parking_slot):
        self.__parking_slot_name = parking_slot

    @property
    def node_id(self):
        return self.__node_id

    @node_id.setter
    def node_id(self, node):
        self.__node_id = node

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, node):
        self.__node = node

    @property
    def record_status(self):
        return self.__record_status

    @record_status.setter
    def record_status(self, record_status):
        self.__record_status = record_status

    def __eq__(self, other):
        return self.__id == other.id\
               and self.__first_name == other.first_name \
               and self.__second_name == other.second_name \
               and self.__address == other.address \
               and self.__phone == other.phone \
               and self.__email == other.email \
               and self.__user_name == other.user_name \
               and self.__password == other.password \
               and self.__pin == other.pin \
               and self.__user_status == other.user_status \
               and self.__parking_slot_name == other.parking_slot \
               and self.__node == other.node \
               and self.__record_status == other.record_status

    @property
    def __str__(self):
        node_name = ""
        node_address = "NOT CONFIGURED"
        if self.__node is not None:
            node_name = str(self.__node.name)
            node_address = " (Address -> " + self.__node.address + ")"
        if self.__user_status:
            user_status_text = 'ON'
        else:
            user_status_text = 'OFF'
        if self.__record_status:
            record_status_text = 'ON'
        else:
            record_status_text = 'OFF'
        tab = '\n' + '\t' * 2
        field_0 = user_fields[0] + '# ' + str(self.__id)
        field_1 = user_fields[1] + ' -> \'' + self.__first_name + '\''
        field_2 = user_fields[2] + ' -> \'' + self.__second_name + '\''
        field_3 = user_fields[3] + ' -> \'' + self.__address + '\''
        field_4 = user_fields[4] + ' -> ' + self.__phone
        field_5 = user_fields[5] + ' -> \'' + self.__email + '\''
        field_6 = tab + user_fields[6] + ' -> \'' + self.__user_name + '\''
        field_7 = user_fields[7] + ' -> \'' + self.__password + '\''
        field_8 = user_fields[8] + ' -> \'' + self.__pin + '\''
        field_9 = user_fields[9] + ' -> ' + user_status_text
        field_10 = user_fields[10] + ' -> ' + str(self.__parking_slot_name)
        field_11 = user_fields[11] + ' ID# ' + ' -> ' + str(self.__node_id)
        field_11_link = user_fields[11] + ' -> ' + node_name + node_address
        field_12 = tab + user_fields[12] + ' -> ' + record_status_text
        return ",\t".join([field_0, field_1, field_2, field_3, field_4,
                           field_5, field_6, field_7, field_8, field_9,
                           field_10, field_11, field_11_link, field_12])

    def get_user_to_show_in_table(self):
        to_show = list()
        to_show.append(self.__id)
        for column_num in user_fields_to_show:
            if column_num == 0:
                to_show.append(str(self.__id))
            if column_num == 1:
                to_show.append(self.__first_name)
            if column_num == 2:
                to_show.append(str(self.__second_name))
            if column_num == 3:
                to_show.append(self.__address)
            if column_num == 4:
                to_show.append(self.__phone)
            if column_num == 5:
                to_show.append(self.__email)
            if column_num == 6:
                to_show.append(self.__user_name)
            if column_num == 7:
                to_show.append(self.pass_to_show())
                # to_show.append(self.__password)
            if column_num == 8:
                to_show.append(self.__pin)
            if column_num == 9:
                if self.__user_status:
                    to_show.append("Yes")
                else:
                    to_show.append("No")
            if column_num == 10:
                to_show.append(self.__parking_slot_name)
            if column_num == 11:
                to_show.append(str(self.__node_id))
        return to_show


class Users:

    def __init__(self, nodes_assigned, path=CSV_PATH + USERS_CSV):
        self.__users = self.__read_csv(nodes_assigned, path)

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, users_list):
        self.__users = users_list

    def __eq__(self, other):
        res = len(self.__users) == len(other.users)
        if res:
            for count, line in enumerate(self.__users):
                res &= self.__users[count] == other.users[count]
        return res

    def __str__(self):
        users_str = ""
        for user in self.__users:
            users_str += '\n' + user.__str__
        return users_str

    def __getitem__(self, item):
        if item < len(self.__users):
            return self.__users[item]
        else:
            return None

    @staticmethod
    def __read_csv(nodes_configured, path):
        read_users = list()

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_count = 0
            for row in csv_reader:
                column_count = 0
                for column in row:
                    if row_count == 0:
                        try:
                            if column != user_fields[column_count]:
                                msg = "CHECK COLUMN NAMES IN THE FILE -> %s"
                                raise Exception(msg % USERS_CSV)
                        except Exception as e:
                            print(e)
                    else:
                        if column_count == 0:           # ID
                            new_user = User(int(column))
                        elif column_count == 1:         # User First Name
                            new_user.first_name = column
                        elif column_count == 2:         # User Second Name
                            new_user.second_name = column
                        elif column_count == 3:         # User Address
                            new_user.address = column
                        elif column_count == 4:         # User Phone
                            new_user.phone = column
                        elif column_count == 5:         # User Email
                            new_user.email = column
                        elif column_count == 6:         # User Entry Name
                            new_user.user_name = column
                        elif column_count == 7:         # User Password
                            new_user.password = column
                        elif column_count == 8:         # User PIN
                            new_user.pin = column
                        elif column_count == 9:         # User Status
                            new_user.user_status = column.upper() == 'ON'
                        elif column_count == 10:        # User Parking Slot
                            new_user.parking_slot = column
                        elif column_count == 11:        # User's Node assigned
                            new_user.node_id = int(column)
                            if nodes_configured is not None:
                                index = new_user.node_id - 1
                                new_user.node = nodes_configured[index]
                        elif column_count == 12:        # User Record Status
                            new_user.record_status = column.upper() == 'ON'
                            read_users.append(new_user)
                    column_count += 1
                row_count += 1
        return read_users

    def save(self, path=''):
        if path == '':
            path_to_save = path
        else:
            path_to_save = path + '\\'
        self.__write_csv(CSV_PATH + path_to_save + USERS_CSV)

    def __write_csv(self, path):
        with open(path, mode='w') as write_file:
            csv_writer = csv.writer(write_file,
                                    delimiter=',',
                                    lineterminator='\n')
            csv_writer.writerow(user_fields)
            for user in self.__users:
                if user.user_status:
                    user_status_text = "ON"
                else:
                    user_status_text = "OFF"
                if user.record_status:
                    record_status_text = "ON"
                else:
                    record_status_text = "OFF"
                csv_writer.writerow([str(user.id),
                                     user.first_name, user.second_name,
                                     user.address, user.phone, user.email,
                                     user.user_name, user.password, user.pin,
                                     user_status_text, user.parking_slot,
                                     str(user.node_id), record_status_text])

    def get_all_to_show_in_table(self):
        res = list()
        num = 0
        for user in self.__users:
            user_text = user.get_user_to_show_in_table()
            if user.record_status:
                num += 1
                user_text[0] = str(num)
                res.append(user_text)
        return res


if __name__ == '__main__':
    power_lines = pl.PowerLines()
    all_nodes = nodes.Nodes(power_lines)
    all_users = Users(all_nodes)
    print(all_users)
    power_lines_test = pl.PowerLines(CSV_PATH + "Test\\" + POWER_LINES_CSV)
    nodes_test = nodes.Nodes(power_lines_test, CSV_PATH + "Test\\" + NODES_CSV)
    users_test = Users(nodes_test)
    print(users_test)
    print(all_users == users_test)
    users_test.save("Test1")
    users_check = Users(nodes_test, CSV_PATH + "Test1\\" + USERS_CSV)
    print(users_check)
    print(users_test == users_check)
