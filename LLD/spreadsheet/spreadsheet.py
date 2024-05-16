class Cell:
    def __init__(self, data_type=None):
        self.value = None
        self.data_type = data_type

    def set_value(self, value):
        if self.data_type and not isinstance(value, self.data_type):
            raise TypeError(f"Expected value of type {self.data_type.__name__}, got {type(value).__name__}")
        self.value = value

    def get_value(self):
        return self.value

    def set_type(self, data_type):
        if self.value is not None and not isinstance(self.value, data_type):
            raise TypeError(f"Existing value of type {type(self.value).__name__} cannot be converted to {data_type.__name__}")
        self.data_type = data_type


class Column:
    def __init__(self, rows, name="", data_type=None):
        self.name = name
        self.data_type = data_type
        self.cells = [Cell(data_type) for _ in range(rows)]

    def set_name(self, name):
        self.name = name

    def set_type(self, data_type):
        for cell in self.cells:
            cell.set_type(data_type)
        self.data_type = data_type

    def get_cell(self, index):
        if index < 0 or index >= len(self.cells):
            raise IndexError("Cell index out of range")
        return self.cells[index]


class Spreadsheet:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = [Column(rows) for _ in range(columns)]

    def set_column_name(self, column_index, name):
        if column_index < 0 or column_index >= len(self.columns):
            raise ValueError("Column index out of range")
        self.columns[column_index].set_name(name)

    def set_column_type(self, column_index, data_type):
        if column_index < 0 or column_index >= len(self.columns):
            raise ValueError("Column index out of range")
        self.columns[column_index].set_type(data_type)

    def update_column(self, column_index, name, data_type):
        if column_index < 0 or column_index >= len(self.columns):
            raise ValueError("Column index out of range")
        self.columns[column_index].set_name(name)
        self.columns[column_index].set_type(data_type)

    def set_value(self, row, column, value):
        if row < 0 or row >= self.rows or column < 0 or column >= len(self.columns):
            raise ValueError("Row or column index out of range")
        self.columns[column].get_cell(row).set_value(value)

    def get_value(self, row, column):
        if row < 0 or row >= self.rows or column < 0 or column >= len(self.columns):
            raise ValueError("Row or column index out of range")
        return self.columns[column].get_cell(row).get_value()

    def display(self):
        # Display column names
        print([column.name for column in self.columns])
        # Display rows
        for i in range(self.rows):
            print([self.columns[col].get_cell(i).get_value() for col in range(len(self.columns))])


# Example usage
sheet = Spreadsheet(3, 3)

# Update column name and type
sheet.update_column(0, "Integer Column", int)
sheet.update_column(1, "Float Column", float)
sheet.update_column(2, "String Column", str)

try:
    sheet.set_value(0, 0, "hello")  # This should raise TypeError because the column expects int
except TypeError as e:
    print("Caught an error while setting value:", e)

sheet.set_value(1, 0, 10)
sheet.set_value(1, 1, 3.14)
sheet.set_value(1, 2, "world")

sheet.display()  # Display the spreadsheet

try:
    sheet.set_value(0, 0, "hello")  # This should raise TypeError because the column expects int
except TypeError as e:
    print("Caught an error while setting value:", e)

sheet.display()  # Display the spreadsheet
