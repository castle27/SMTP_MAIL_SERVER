import sys
import smtpd
import asyncore
from PyQt4 import QtGui


class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message data        :', data
        return

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.button)
        layout.addWidget(self.edit)
        self.setWindowTitle("PYTHON SERVER")
        self.button.clicked.connect(self.handleTest)

    def handleTest(self):
        server = CustomSMTPServer(('127.0.0.1', 1025), None)
        asyncore.loop(count=9)
        self.edit.append('server server server')
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
