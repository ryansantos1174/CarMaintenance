from  PyQt5 import QtWidgets 
from  PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QPixmap, QFont
import sys
from PyQt5.uic import loadUi
import xml.etree.ElementTree as ET
import os



class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        loadUi("untitled.ui", self)
        self.connectButtons()
        self.show()

    def connectButtons(self):
        currentDate = QDateTime().currentDateTime().toString("MM/dd/yyyy")
        self.dateLineEdit.setText(currentDate)
        self.saveButton.clicked.connect(self.saveData)

    def saveData(self):
        if not os.path.exists("./MaintenanceRecords.xml"):
            data = ET.Element('Record')
            maintenanceType = ET.SubElement(data, "MaintenanceType")
            maintenanceDate  = ET.SubElement(data, "Date")
            maintenanceNotes = ET.SubElement(data, "Notes")

            maintenanceType.text = self.maintenanceComboBox.currentText()
            maintenanceDate.text = self.dateLineEdit.text()
            maintenanceNotes.text = self.textEdit.toPlainText()

            xml = ET.tostring(data)

            with open('MaintenanceRecords.xml', "wb") as f:
                f.write(xml)

        



        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())