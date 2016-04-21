from PyQt4 import QtGui, QtCore
import sys
import design
import jsoncreator
import requests
import re

class TestApp(QtGui.QMainWindow, design.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.setupUi(self)
        self.json_work = None
        self.pushButton.clicked.connect(self.get_account)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        
        
    def get_account(self):
        
        secretKey = self.lineEdit.text()
        publicKey = self.lineEdit_2.text()
        httpAddress = self.lineEdit_3.text()
        
        payload = {'secret_key':secretKey, 'public_key':publicKey}
        r = requests.get(httpAddress + 'account', params=payload, verify=False)
        
        index = r.text.split('"')
        userID = index[17]
        userName = index[21]
        userUUID = index[29]
        
        self.textEdit.setText(r.text+ "\n\n\n" + "User ID: " + userID + "\nUser Name: " + userName + "\nUser UUID: " + userUUID)
        
        
    def file_open(self):
       self.json_work = JsonCreator()
       self.json_work.show()
        
        
    def close_application(self):
        #popup messegae before exiting
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
        
        
class JsonCreator(QtGui.QMainWindow, jsoncreator.Ui_JsonCreator):
    def __init__(self, parent=None):
        super(JsonCreator, self).__init__(parent)
        self.setupUi(self)
        self.json_work = None
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()