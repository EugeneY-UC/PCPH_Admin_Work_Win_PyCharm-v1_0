# -*- coding: utf-8 -*-

import csv
from csvfiles import CSV_PATH, ACCESS_DAILY_CSV

node_access_fields = "ID", "Access Status", "Time", "Access Type"


class NodeAccessDaily:

    def __init__(self, access_id=0):
        self.__id = access_id
        self.__active = False
        self.__access_timetable = list(())

    @property
    def id(self):
        return self.__id

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def access_timetable(self):
        return self.__access_timetable

    @access_timetable.setter
    def access_timetable(self, access_timetable):
        self.__access_timetable = access_timetable

    def __eq__(self, other):
        return self.__id == other.id and self.__active == other.active and \
               self.__access_timetable == other.access_timetable

    def __str__(self):
        str_timetable = ""
        i = 0
        for timetable_row in self.__access_timetable:
            if i > 0:
                str_timetable += '\t' * 8
            str_timetable += node_access_fields[2] + " -> " + timetable_row[0]
            str_timetable += ",\t" + node_access_fields[3] + " -> " + timetable_row[1]
            if i < len(self.__access_timetable) - 1:
                str_timetable += "\n"
            i += 1
        return ",\t".join([node_access_fields[0] + "# " + str(self.__id),
                           node_access_fields[1] + " -> " + str(self.__active),
                           str_timetable])


class AllNodeAccessDaily:

    def __init__(self, path=CSV_PATH + ACCESS_DAILY_CSV):
        self.__all_daily = self.__read_csv(path)

    @property
    def all_daily(self):
        return self.__all_daily

    @all_daily.setter
    def all_daily(self, all_daily):
        self.__all_daily = all_daily

    def __str__(self):
        daily_str = ''
        for daily in self.__all_daily:
            daily_str += '\n' + daily.__str__()
        return daily_str

    def __eq__(self, other):
        res = True
        for count in range(len(self.__all_daily)):
            res &= self.__all_daily[count] == other.all_daily[count]
        return res

    @staticmethod
    def __read_csv(path):
        all_daily_access = list()
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            all_daily_count = -1
            new_node_daily_access = None
            row_count = 0
            one_daily_row_count = 0
            for row in csv_reader:
                if row_count == 0:
                    column_count = 0
                    for column in row:
                        try:
                            if column != node_access_fields[column_count]:
                                raise Exception("CHECK COLUMN NAMES IN THE FILE -> %s, Column# %d"
                                                % (ACCESS_DAILY_CSV, column_count))
                        except Exception as e:
                            print(e)
                        column_count += 1
                    row_count = 1
                else:
                    column_count = 0
                    for column in row:
                        if column_count == 0:                                                           # ID
                            if column != '':
                                if all_daily_count >= 0:
                                    all_daily_access.append(new_node_daily_access)
                                all_daily_count += 1
                                one_daily_row_count = 0
                                new_node_daily_access = NodeAccessDaily(int(column))
                        elif column_count == 1:                                                         # Access Status
                            if one_daily_row_count == 0:
                                new_node_daily_access.active = column == 'ON'
                        elif column_count == 2:                                                         # Time
                            new_node_daily_access.access_timetable.append(list())
                            new_node_daily_access.access_timetable[one_daily_row_count].append(column)
                        elif column_count == 3:                                                         # Access Type
                            new_node_daily_access.access_timetable[one_daily_row_count].append(column)
                        column_count += 1
                    row_count += 1
                    one_daily_row_count += 1
            all_daily_access.append(new_node_daily_access)
        return all_daily_access

    def save(self, path=CSV_PATH + ACCESS_DAILY_CSV):
        self.__write_csv(path)

    def __write_csv(self, path):

        def status_to_str(status):
            if status:
                return "ON"
            else:
                return "OFF"

        with open(path, mode='w') as write_file:
            csv_writer = csv.writer(write_file, delimiter=',', lineterminator='\n')
            csv_writer.writerow(node_access_fields)
            for daily in self.__all_daily:
                for i, time_point in enumerate(daily.access_timetable):
                    if i == 0:
                        csv_writer.writerow([str(daily.id), status_to_str(daily.active),
                                             str(time_point[0]), str(time_point[1])])
                    else:
                        csv_writer.writerow(['', '', str(time_point[0]), str(time_point[1])])


if __name__ == "__main__":
    all_node_access_daily = AllNodeAccessDaily()
    print(all_node_access_daily)
    node_access_test = AllNodeAccessDaily(CSV_PATH + "Test\\" + ACCESS_DAILY_CSV)
    print(node_access_test)
    print(all_node_access_daily == node_access_test)
    node_access_test.save(CSV_PATH + "Test1\\" + ACCESS_DAILY_CSV)
    node_access_test1 = AllNodeAccessDaily(CSV_PATH + "Test1\\" + ACCESS_DAILY_CSV)
    print(node_access_test1)
    print(node_access_test == node_access_test1)
