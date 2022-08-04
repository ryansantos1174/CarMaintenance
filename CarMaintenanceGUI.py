from  PyQt5 import QtWidgets 
from  PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QPixmap, QFont
import sys
from PyQt5.uic import loadUi
import xml.etree.ElementTree as ET
import os
import DataWindow



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
        self.pushButton.clicked.connect(self.showRecords)

    def saveData(self):
        if not os.path.exists('./MaintenanceRecords.xml') or os.stat('./MaintenanceRecords.xml').st_size==0:
            data = ET.Element('Records')
            maintenance = ET.SubElement(data, "Maintenance")
            maintenanceType = ET.SubElement(maintenance, "MaintenanceType")
            maintenanceDate  = ET.SubElement(maintenance, "Date")
            maintenanceNotes = ET.SubElement(maintenance, "Notes")

            maintenanceType.text = self.maintenanceComboBox.currentText()
            maintenanceDate.text = self.dateLineEdit.text()
            maintenanceNotes.text = self.textEdit.toPlainText()

            xml = ET.tostring(data)
            with open('MaintenanceRecords.xml', "wb") as f:
                 f.write(xml)
        else:
            tree = ET.parse("MaintenanceRecords.xml")
            xmlRoot = tree.getroot()
            maintenance = ET.Element("Maintenance")
            maintenanceType = ET.SubElement(maintenance, "MaintenanceType")
            maintenanceDate  = ET.SubElement(maintenance, "Date")
            maintenanceNotes = ET.SubElement(maintenance, "Notes")
            maintenanceType.text = self.maintenanceComboBox.currentText()
            maintenanceDate.text = self.dateLineEdit.text()
            maintenanceNotes.text = self.textEdit.toPlainText()
            xmlRoot.append(maintenance)
            tree.write('MaintenanceRecords.xml')


            

    def showRecords(self):
        tree = ET.parse('MaintenanceRecords.xml')
        root = tree.getroot()
        dataDict = {}
        for i, child in enumerate(root):
            entry = {}
            for j, data in enumerate(child):
                entry[data.tag] = data.text
            dataDict[str(i)]= entry
        self.data = DataWindow.DataWin(dataDict, len(root), len(root[0]))
        
        


        



        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()
    sys.exit(app.exec_())