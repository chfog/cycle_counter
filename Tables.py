


class Table():

    def __init__(self, header = [], rows = []):
        self.header = header
        self.width = length(header)
        self.length = 0
        self.header_dict = dict(enumerate(header))
        self.rows = []
        self.add_rows(rows)
        ## may have problems if multiple isbns are on a csv


    def add_row(self, row):
        if len(row) == self.width:
            self.rows += [row]
            self.length += 1
        else:
            print("row width doesn't match" + row)

    def add_rows(self, rows):
        for row in rows:
            if row[0] == self.header[0]:
                pass
            else:
                self.add_row(row)


    def add_col(self, col_name, col = []):
        if col_name in self.header_dict:
            print("Column " + col_name + " already in table.")

        elif col == []:
            self.header.append(col_name)
            self.header_dict[col_name] = self.length
            self.length += 1
            for row in self.rows:
                row += []

        elif len(col) == self.length:
            self.header.append(col_name)
            self.header_dict[col_name] = self.length
            self.length += 1

            for i in range(self.length):
                self.rows[i] += [col(i)]

            else:
                pass
        else:
            print("column length doesn't match")


    def get_col(self, col_name):
        if self.has_col(col_name):
            return list(map(lambda x: x[self.header_dict[col_name]]))
        else:
            print("no column with name" + col_name)

    def has_col(self, col_name):
        return col_name in self.header_dict

    def col_number(self, col_name):
        if self.has_col(col_name):
            return self.header_dict[col_name]
        else:
            print("no column with name" + col_name)

    def get_header(self):
        return self.header

    def get_complete_table(self):
        return self.header + self.rows

    def rows(self):
        return self.rows

    def with_columns(self, columns = None):
        if columns == None:
            return self
        else:
            new = Table([])
            for col in columns:
                new.add_col(col, self.get_col(col))
            return new

    def add_table(self, other):
        if self.get_header() == other.get_header():
            for row in other.rows():
                self.add_row(row)
        elif self.get_header() == []:
            self = other
        else: print("Headers", self.get_header(), ",", other.get_header(), "do not match.")
