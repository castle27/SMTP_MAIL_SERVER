import sys
from PyQt4 import QtGui

import subprocess

class Window(QtGui.QWidget):
    def __init__(self):
        
        
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.setWindowTitle("PYTHON CLIENT")
        self.button1 = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.edit)
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.handleTest)
        
        self.button2 = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.edit)
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.handleTest)
        
        
        

    def handleTest(self):
        
        self.edit.append("client client client")
        
        
        execfile('cli.py')



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())