from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.layout = QGridLayout()
        self.setupWindow()
        self.setLayout(self.layout)
        
       
#FIXME The text area is very large on the window
#FIXME The text in QTextEdit is not in the background, it automatically fills the table
    def setupWindow(self):
        self.setGeometry(700,200,500, 500)
        self.setWindowTitle("Car Maintenance")
        self.carMakeLabel = QLabel("Enter your Car Make: ")
        self.carMakeText = QTextEdit("Car Make")
        self.carModelLabel = QLabel("Enter your car model here: ")
        self.carModelText = QTextEdit("Car Model")
        self.carYearLabel = QLabel("Enter your car year here: ")
        self.carYearText = QTextEdit("Car Year")
        self.submitButton = QPushButton("Submit")


        self.carMakeText.setMaximumHeight(40)
        self.carMakeText.setMaximumWidth(400)
        self.carModelText.setMaximumHeight(40)
        self.carModelText.setMaximumWidth(400)
        self.carYearText.setMaximumHeight(40)
        self.carYearText.setMaximumWidth(400)


        self.layout.addWidget(self.carMakeLabel, 0, 0)
        self.layout.addWidget(self.carMakeText, 0, 1)
        self.layout.addWidget(self.carModelLabel, 1, 0)
        self.layout.addWidget(self.carModelText, 1, 1)
        self.layout.addWidget(self.carYearLabel, 2, 0)
        self.layout.addWidget(self.carYearText, 2, 1)
        self.layout.addWidget(self.submitButton, 3, 0, 1, 2)
       



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())  