# -*- coding: utf-8 -*-

import csv
from csvfiles import CSV_PATH, USERS_CSV

user_fields = ("ID", "Address", "First Name", "Second Name", "Phone", "Email",
               "User Name", "Pass", "Pin", "User Status", "Parking Slot",
               "Node", "Record Status")


class User:

    def __init__(self, user_id=0):
        self.__id = user_id
        self.__address = ""
        self.__first_name = ''
        self.__second_name = ''
        self.__phone = 0
        self.__email = ''
        self.__user_name = ''
        self.__password = ''
        self.__pin = ''
        self.__user_status = False
        self.__parking_slot = 0
        self.__node = None
        self.__record_status = False

    @property
    def id(self):
        return self.__id

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

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
        return self.__parking_slot

    @parking_slot.setter
    def parking_slot(self, parking_slot):
        self.__parking_slot = parking_slot

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
        return self.__id == other.id and self.__address == other.address\
               and self.__first_name == other.first_name\
               and self.__second_name == other.second_name\
               and self.__phone == other.phone\
               and self.__email == other.email\
               and self.__user_name == other.user_name\
               and self.__password == other.password\
               and self.__pin == other.pin\
               and self.__user_status == other.user_status\
               and self.__parking_slot == other.parking_slot\
               and self.__node == other.node\
               and self.__record_status == other.record_status

    def __str__(self):
        address_txt = ''
        if self.__address is not None:
            address_txt = str(self.__address)
        parking_slot_txt = ''
        if self.__parking_slot is not None:
            parking_slot_txt = str(self.__parking_slot)
        return ",\t".join([user_fields[0] + '# ' + str(self.__id),
                           user_fields[1][:-3] + ' -> ' + address_txt,
                           user_fields[2][:-3] + ' -> ' + parking_slot_txt])


class Users:

    def __init__(self, node_assigned, path=CSV_PATH + USERS_CSV):
        self.__users = self.__read_csv(node_assigned, path)

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
            users_str += '\n' + user.__str__()
        return users_str

    @staticmethod
    def _read_csv(path):
        users = list()
        return users
