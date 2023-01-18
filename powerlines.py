# -*- coding: utf-8 -*-

import csv
from csvfiles import CSV_PATH, POWER_LINES_CSV

power_line_fields = "ID", "Line Name", "Max AMP", "Active", "Record Status"
power_line_fields_to_show = range(4)


def get_power_lines_header():
    to_show = list()
    to_show.append('#')
    for column_num in power_line_fields_to_show:
        to_show.append(power_line_fields[column_num])
    return to_show


class PowerLine:

    def __init__(self, line_id=0):
        self.__id = line_id
        self.__name = ''
        self.__max_amp = 0
        self.__active = False
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
    def max_amp(self):
        return self.__max_amp

    @max_amp.setter
    def max_amp(self, max_amp):
        self.__max_amp = max_amp

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active

    @property
    def record_status(self):
        return self.__record_status

    @record_status.setter
    def record_status(self, record_status):
        self.__record_status = record_status

    def __eq__(self, other):
        return self.__id == other.id and self.__name == other.name \
                            and self.__max_amp == other.max_amp \
                            and self.__active == other.active \
                            and self.__record_status == other.record_status

    def __str__(self):
        field_0 = power_line_fields[0] + '# ' + str(self.__id)
        field_1 = power_line_fields[1] + ' -> \'' + self.__name + '\''
        field_2 = '\n' + '\t' * 2 + power_line_fields[2] + ' -> '\
                  + str(self.__max_amp)
        field_3 = power_line_fields[3] + ' ->  ' + str(self.__active)
        field_4 = power_line_fields[4] + ' -> ' + str(self.__record_status)
        return ",\t".join([field_0, field_1, field_2, field_3, field_4])

    def get_line_to_show_in_table(self):
        to_show = list()
        to_show.append(self.__id)
        for column_num in power_line_fields_to_show:
            if column_num == 0:
                to_show.append(str(self.__id))
            if column_num == 1:
                to_show.append(self.__name)
            if column_num == 2:
                to_show.append(str(self.__max_amp))
            if column_num == 3:
                if self.__active:
                    to_show.append("Yes")
                else:
                    to_show.append("No")
        return to_show


class PowerLines:

    def __init__(self, path=CSV_PATH + POWER_LINES_CSV):
        self.__lines = self.__read_csv(path)

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, lines):
        self.__lines = lines

    def __eq__(self, other):
        if len(self.__lines) != len(other.__lines):
            return False
        res = True
        for count, line in enumerate(self.__lines):
            res &= self.__lines[count] == other.__lines[count]
        return res

    def __str__(self):
        power_lines_str = ""
        for line in self.__lines:
            power_lines_str += '\n' + line.__str__()
        return power_lines_str

    def __getitem__(self, item):
        if item < len(self.__lines):
            return self.__lines[item]
        else:
            return None

    def __iter__(self):
        return PowerLinesIterator(self)

    @staticmethod
    def __read_csv(path):
        lines = list()
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            row_count = 0
            for row in csv_reader:
                column_count = 0
                for column in row:
                    if row_count == 0:
                        try:
                            if column != power_line_fields[column_count]:
                                msg = "CHECK COLUMN NAMES IN THE FILE -> %s"
                                raise Exception(msg % POWER_LINES_CSV)
                        except Exception as e:
                            print(e)
                    else:
                        if column_count == 0:                   # ID
                            new_line = PowerLine(int(column))
                        elif column_count == 1:                 # Line Name
                            new_line.name = column
                        elif column_count == 2:                 # Max AMP
                            new_line.max_amp = int(column)
                        elif column_count == 3:                 # Active
                            new_line.active = column.upper() == 'ON'
                        elif column_count == 4:                 # Record Status
                            new_line.record_status = column.upper() == 'ON'
                            lines.append(new_line)
                    column_count += 1
                row_count += 1
        return lines

    def save(self, path=CSV_PATH + POWER_LINES_CSV):
        self.__write_csv(path)

    def __write_csv(self, path):
        with open(path, mode='w') as write_file:
            csv_writer = csv.writer(write_file,
                                    delimiter=',',
                                    lineterminator='\n')
            csv_writer.writerow(power_line_fields)
            for line in self.__lines:
                if line.active:
                    str_active = 'ON'
                else:
                    str_active = 'OFF'
                if line.record_status:
                    str_record_status = 'ON'
                else:
                    str_record_status = 'OFF'
                csv_writer.writerow([str(line.id),
                                     line.name,
                                     str(line.max_amp),
                                     str_active,
                                     str_record_status])

    def get_all_to_show_in_table(self):
        res = list()
        num = 0
        for line in self.__lines:
            line_text = line.get_line_to_show_in_table()
            if line.record_status:
                num += 1
                line_text[0] = str(num)
                res.append(line_text)
        return res


class PowerLinesIterator:

    def __init__(self, power_lines_iterated):
        self._power_lines = power_lines_iterated
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            n = self._power_lines[self.index]
            self.index += 1
            return n
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    power_lines = PowerLines()
    print(power_lines)
    power_lines_test = PowerLines(CSV_PATH + "Test\\" + POWER_LINES_CSV)
    print(power_lines_test)
    print(power_lines == power_lines_test)
    power_lines_test.save(CSV_PATH + "Test1\\" + POWER_LINES_CSV)
    power_lines_test1 = PowerLines(CSV_PATH + "Test1\\" + POWER_LINES_CSV)
    print(power_lines_test1)
    print(power_lines_test == power_lines_test1)
