from PyQt4 import QtGui, QtCore
import sys
import design
import jsoncreator
import new_line
import requests
import re
import json
import time
from new_jasoncreator import JsonCreator
from class_test import Response, GetMethod, PostMethod
from doctest import testfile
#from idlelib.ClassBrowser import file_open
from PyQt4.Qt import QListWidgetItem
from PyQt4.QtCore import QThread

#class MethodSend(QThread):
 #   def __init__(self, data):
       # QThread.__init__(self)
       # self.data = data
        
    #def run(self):
        
        #for dataLine in self.data:
            #print ("\n" + str(dataLine) + "\n")
            #time.sleep(1)
            

class TestApp(QtGui.QMainWindow, design.Ui_Dialog):
    def __init__(self, parent=None):
        super(TestApp, self).__init__(parent)
        self.setupUi(self)
        
        global txtFilePath
        txtFilePath = []
        
        global txtFileUUID
        txtFileUUID = []
        
        global uploadFileUUID
        uploadFileUUID = []
        
        global testFilePath
        testFilePath = []
        
        global testFile
        testFile = None
        
        
        
        self.json_work = JsonCreator(testFile)
        self.new_line_window = None
        self.startBtn.clicked.connect(self.start_test)
        self.pushButton_2.clicked.connect(self.close_application)
        self.fileLoad.clicked.connect(self.file_open)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.loadTxtBtn.clicked.connect(self.open_txt)
        self.loadFileBtn.clicked.connect(self.open_test_files)
    
        
    def start_test(self):
        global txtFilePath
        global txtFileUUID
        global testFilePath
        global uploadFileUUID
        
        startFlag = 0
        
        if (self.json_work.testFile):
            startFlag = 1
        else:
            choice = QtGui.QMessageBox.question(self, 'No File', "No file was loaded, would you like to load?",
                                                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
            if choice == QtGui.QMessageBox.Yes:
                self.json_work = JsonCreator(testFile)
                self.json_work.show()
            else:
                pass
        
        
        
        if startFlag == 1:
            
            self.textEdit.append("NEW TEST\n")
            secretKey = self.lineEdit.text()
            publicKey = self.lineEdit_2.text()
            httpAddress = self.lineEdit_3.text()
            payload = dict() 
            errorFlag = [False]
            #uuidToAddress = 0
            prevResponse = {}
            prevPayload = ()
            
            with open(self.json_work.testFile) as codeLines_data:
                data = json.load(codeLines_data)
                
            #self.thread = MethodSend(data["data"])
            #self.thread.start() 

            #while not self.thread.isFinished():
                #time.sleep(0.5)
                #print ("\nChecked\n")
                
            for lineIndex in range(len(data["data"])):  
                
                
                
                #Get line code
                if str.lower(data["data"][lineIndex]["method"]) == 'get':
                    #payload initialization
                    
                    checkLine = GetMethod(data["data"][lineIndex])
                    checkLine.get_method(secretKey, publicKey, httpAddress, errorFlag, prevResponse, prevPayload, self.textEdit, lineIndex)

                #Post line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'post': 
                    checkLine = PostMethod(data["data"][lineIndex]) 
                    checkLine.post_method(secretKey, publicKey, httpAddress, txtFilePath, txtFileUUID, testFilePath, uploadFileUUID, prevResponse, prevPayload, self.textEdit, errorFlag) 
                                                   
                    
                #Delete line code
                elif str.lower(data["data"][lineIndex]["method"]) == 'del': 
                    print("we have a deleter in line: " + str(lineIndex + 1))
                    
                
                if errorFlag[0] == True:
                    break
    
                self.progressBar.setValue((100/(len(data["data"]))*(lineIndex+1)))
                time.sleep(1)
        
        
    def file_open(self): 
        self.json_work = JsonCreator(testFile)
        self.json_work.show()
       
       
        
    def close_application(self):
        #popup messegae before exiting
        choice = QtGui.QMessageBox.question(self, 'Quit', "Quit application?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass
        
    def open_txt(self):
        global txtFilePath
        txtFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.txt")
        txtFilePath.append(txtFile)
        fileName = txtFile.split('/')
        self.txtFilesList.addItem('%s' % fileName[len(fileName)-1])
        
    def open_test_files(self):
        global testFilePath
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        testFilePath.append(testFile)
        fileName = testFile.split('/')
        self.testFilesList.addItem('%s' % fileName[len(fileName)-1])
        
        
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
