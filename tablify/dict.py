

class DictToTable():
    def __init__(self):
        self.initial = '<table border="1">{}</table>'
        self.rows = []
        self.header_template = "<th>{}</th>"
        self.row_template = "<tr>{}</tr>"
        self.data_template = "<td>{}</td>"
    def add_row(self,row_data):
        new_row = self.row_template.format("".join(row_data))
        self.rows.append(new_row)
    def add_data(self,data,is_header):
        header_list = []
        for items in data:
            if is_header:
                header_list.append(self.header_template.format(items))
            else:
                header_list.append(self.data_template.format(items))
        self.add_row(header_list)
        pass
    def commit(self):
        return self.initial.format("".join(self.rows))
