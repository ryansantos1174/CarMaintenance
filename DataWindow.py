from  PyQt5 import QtWidgets 

class DataWin(QtWidgets.QTableWidget):
    def __init__(self, data, *args):
        QtWidgets.QTableWidget.__init__(self, *args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.show()

    def setData(self):
        headers = []
        for i, val in enumerate(self.data[list(self.data.keys())[0]]):
            headers.append(val)
        for i, _ in enumerate(self.data.keys()):
            for j, attribute in enumerate(self.data[_].values()):
                newitem = QtWidgets.QTableWidgetItem(attribute)
                self.setItem(i, j, newitem)
        self.setHorizontalHeaderLabels(headers)        

        # Add sorting function





