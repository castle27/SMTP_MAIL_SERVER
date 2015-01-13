import sys
from PyQt4 import QtGui

import smtplib
import email.utils
from email.mime.text import MIMEText


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        layout = QtGui.QVBoxLayout(self)
        self.button = QtGui.QPushButton('Test')
        self.edit = QtGui.QTextEdit()
        layout.addWidget(self.edit)
        self.setWindowTitle("PYTHON CLIENT")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.handleTest)

    def handleTest(self):
        msg = MIMEText('This is the body of the message.')
        msg['To'] = email.utils.formataddr(('Recipient', 'recipient@example.com'))
        msg['From'] = email.utils.formataddr(('Author', 'author@example.com'))
        msg['Subject'] = 'Simple test message'

        server = smtplib.SMTP('127.0.0.1', 1025)
        server.set_debuglevel(True) 
        try:
            server.sendmail('author@example.com', ['recipient@example.com'], msg.as_string())
        finally:
            server.quit()

        self.edit.append("client client client")

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())