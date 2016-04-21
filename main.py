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
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        
        
    def start_test(self):
        
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
        self.doneBtn.clicked.connect(self.close_window)
        self.loadExFileBtn.clicked.connect(self.load_file)
        self.createNewBtn.clicked.connect(self.new_file)
        self.saveBtn.clicked.connect(self.save_file)
        self.addNewLine.clicked.connect(self.edit_file)
        self.saveNewToFile.clicked.connect(self.saveNewLine_file)
        
        
    def close_window(self):
        self.close()
        
    def load_file(self):
        nameOfFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(nameOfFile, 'r')
        
        with loadedFile:
            text = loadedFile.read()
            
            textSplit = text.split('oid')
            index = len(textSplit)
            self.textEditFileLoad.setText(text)
        
            
    def new_file(self):
        self.textEditFileLoad.setText('{"data":[{"additional_data":{"oid":"1"},}]}')
        
    def save_file(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.json','*.json')
        file = open(fileName, 'w')
        text = self.textEditFileLoad.toPlainText()
        file.write(text)
        file.close()
        
        
    def edit_file(self):
        self.textEditFileLoad.setText('"method":"<GET/POST>","address":"<enter address>"}')
        
    def saveNewLine_file(self):
        
        #read the file
        nameOfFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(nameOfFile, 'r')
        
        #convert to text
        with loadedFile:
            text = loadedFile.read()
            
        #find index number
        textSplit = text.split('oid')
        newIndex = len(textSplit)
        
        #prepare to write
        loadedFile = open(nameOfFile, 'w')
        currentText = self.textEditFileLoad.toPlainText()
        
        #find the place where to add the new line
        fileEnd = len(text)-1
        
        #create new text
        newText = text[:fileEnd] + ',{"additional_data":{"oid":"' + str(newIndex) + '"},' + currentText + text[fileEnd:]
        
        #overwrite the existing file with new content
        loadedFile.write(newText)
        loadedFile.close()
        
        self.textEditFileLoad.setText(newText)
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()