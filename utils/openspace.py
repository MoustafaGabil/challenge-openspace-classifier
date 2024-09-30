from table import Table


class Openspace:
    def __init__(self, tables_num=6):
        self.tables_num = tables_num
        self.tables = []
        for x in range(tables_num):
            self.tables.append(Table())

    def organize(self, names):
        self.names = names
        self.first_table = []

        for name in self.names:
            for table in self.tables:
                for seat in Table.assign_seat():
                    self.first_table.append(Table.assign_seat())
        return self.first_table


Lists = ["Majed", "Minah", "Amr", "JAck", "Leon"]
open_1 = Openspace()
print(open_1.organize(Lists))
#     for i in names:
#         for j in self.tables:
#            j.append(Table.assign_seat())


# def display(self):
#     for i in self.tables:
#                 print(f"Table {i+1}:")
#                 j=0
#                 for j in self.tables[k]:
#                     print(f"  Seat {j+1}: {seat()}")

#                 k = k+1
