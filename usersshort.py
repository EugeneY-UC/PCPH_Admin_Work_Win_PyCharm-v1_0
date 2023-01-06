# -*- coding: utf-8 -*-

import csv

user_short_fields = "User#", "PIN", "Node#"


class UserShort:

    def __init__(self, user_id=0):

        self.__id = user_id
        self.__pin = ''
        self.__node = 0

    @property
    def id(self):
        return self.__id

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def node(self):
        return self.__node

    @node.setter
    def node(self, node):
        self.__node = node

    def __str__(self):
        return ",\t".join([user_short_fields[0] + ' -> ' + str(self.__id),
                           user_short_fields[1] + ' -> ' + str(self.__pin).zfill(4),
                           user_short_fields[2] + ' -> ' + str(self.__node)])


class UsersShort:

    def __init__(self, path='CSV\\user_test.csv'):
        self.__users = self.__read_csv(path)

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, users_list):
        self.__users = users_list

    def __str__(self):
        users_str = ''
        for user in self.__users:
            users_str += '\n' + user.__str__()
        return users_str

    @staticmethod
    def __read_csv(path):
        new_users = list()
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_count = 0
            for row in csv_reader:
                column_count = 0
                for column in row:
                    if row_count > 0:
                        if column_count == 0:  # ID
                            new_user = UserShort(int(column))
                        elif column_count == 1:  # PIN
                            new_user.pin = column
                        elif column_count == 2:  # Charger Node Address
                            new_user.node = column
                            new_users.append(new_user)
                    column_count += 1
                row_count += 1
        return new_users

    def save(self, path='CSV\\Test1\\user_test.csv'):
        self.__write_csv(path)

    def __write_csv(self, path):
        with open(path, mode='w') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', lineterminator='\n')
            csv_writer.writerow(user_short_fields)
            for user in self.__users:
                csv_writer.writerow([str(user.id), user.pin, str(user.node)])


if __name__ == "__main__":
    users = UsersShort()
    print(users)
    users_test = UsersShort("CSV\\Test\\user_test.csv")
    print(users_test)
    users_test.save()
    users_test1 = UsersShort("CSV\\Test1\\user_test.csv")
    print(users_test1)
