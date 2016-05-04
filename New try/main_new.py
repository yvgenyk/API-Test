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
from class_test import Response, GetMethod
from doctest import testfile
from idlelib.ClassBrowser import file_open
from PyQt4.Qt import QListWidgetItem

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
            choice = QtGui.QMessageBox.question(self, 'No File', "No file was loaded, would you like to load?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
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
            errorFlag = 0
            #uuidToAddress = 0
            prevResponse = {}
            prevPayload = ()
            
            with open(self.json_work.testFile) as codeLines_data:
                data = json.load(codeLines_data)
            for lineIndex in range(len(data["data"])):  
                
                
                
                #Get line code
                if str.lower(data["data"][lineIndex]["method"]) == 'get':
                    #payload initialization
                    
                    checkLine = GetMethod(data["data"][lineIndex])
                    checkLine.get_method(secretKey, publicKey, httpAddress, errorFlag, prevResponse, prevPayload, self.textEdit, lineIndex)
                    #get_method(self, secretKey, secretKey, errorFlag, prevResponse, prevPayload)
                    
                    
                    
                    
                    
                    
                    
                    
                #Post line code
                if str.lower(data["data"][lineIndex]["method"]) == 'post': 
                    payload = dict()
                    uploadedrscFlag = False
                    for payIndex in range(len(data["data"][lineIndex]['params'])):
                    
                        if data["data"][lineIndex]["params"][payIndex] == "secret_key":
                            payload[data["data"][lineIndex]["params"][payIndex]] = secretKey
                            
                        elif data["data"][lineIndex]["params"][payIndex] == "public_key":
                            payload[data["data"][lineIndex]["params"][payIndex]] = publicKey
                            
                            
                        #Text upload  
                        elif data["data"][lineIndex]["params"][payIndex]["name"] == "textrsc":
                            
                            if data["data"][lineIndex]["params"][payIndex]["value"] == "empty":
                                pass
                            elif data["data"][lineIndex]["params"][payIndex]["value"] == "nokey":
                                pass
                            
                            else:
                            
                                if len(txtFilePath) == 0:
                                    self.textEdit.append("No text file was added\n")
                                
                                elif len(txtFilePath) >= 1:
                                
                                    for txtIndex in range(len(txtFilePath)):
                                
                                        loadedFile = open(txtFilePath[txtIndex], 'r')
                                
                                        with loadedFile:
                                            txt = loadedFile.read()
                                    
                                        payload['text'] = txt
                                        
                                        res = Response(requests.post(httpAddress + data["data"][lineIndex]["address"], data=payload, verify=False))
                                        
                                        if data["data"][lineIndex]["save"] == '1':
                                            prevResponse = res.getJson()
                                            prevPayload = payload
                                        
                                        if res.getStatus() == 200:
                                            res.report_line(data["data"][lineIndex]['title'], self.textEdit)
                                
                                            uuidTxt = str(res.getJson()["results"])
                                            txtFileUUID.append(uuidTxt[2:(len(uuidTxt)-2)])
                                            uploadedrscFlag = True
                                            
                                        else:
                                            self.textEdit.append("Error: %d" % res.getStatus())
                                            errorFlag = 1
                            
                        
                        #File upload  
                        elif data["data"][lineIndex]["params"][payIndex]["name"] == "filersc":
                            
                            if data["data"][lineIndex]["params"][payIndex]["value"] == "empty":
                                pass
                            elif data["data"][lineIndex]["params"][payIndex]["value"] == "nokey":
                                pass
                            
                            else:
                                if len(testFilePath) == 0:
                                    self.textEdit.append("No file was selected\n")
                                
                                elif len(testFilePath) >= 1:
                                
                                    for fileIndex in range(len(testFilePath)):
                                
                                        loadedFile = {'@upload': open(testFilePath[fileIndex], 'rb')}
                                        
                                        res = Response(requests.post(httpAddress + data["data"][lineIndex]["address"], files = loadedFile, data = payload, verify=False))
                                        
                                        if data["data"][lineIndex]["save"] == '1':
                                            prevResponse = res.getJson()
                                            prevPayload = payload
                                        
                                        if res.getStatus() == 200:
                                            res.report_line(data["data"][lineIndex]['title'], self.textEdit)
                                
                                            uuidFile = str(res.getJson()["results"])
                                            uploadFileUUID.append(uuidFile[2:(len(uuidFile)-2)])
                                            uploadedrscFlag = True
                    
                                        else:
                                            self.textEdit.append("Error: %d" % res.getStatus())
                                            errorFlag = 1
                 
                        
                        elif data["data"][lineIndex]["params"][payIndex]["name"] == "sources":
                            #Text sources
                            if data["data"][lineIndex]["params"][payIndex]["value"] == "txt":
                                sourcesString = ""
                                if len(txtFileUUID)>1:
                                    for rsc in range(len(txtFileUUID)):
                                        sourcesString += "," + txtFileUUID[rsc]
                                        
                                    payload[data["data"][lineIndex]["params"][payIndex]["name"]] = sourcesString
                                    
                                elif len(txtFileUUID)==1:
                                    payload[data["data"][lineIndex]["params"][payIndex]["name"]] = txtFileUUID[0]
                                
                                elif len(txtFileUUID)==0:
                                    self.textEdit.append("No text resources found!")
                                    errorFlag =1
                                    
                            #File sources
                            else:
                                sourcesString = ""
                                if len(uploadFileUUID)>1:
                                    for rsc in range(len(uploadFileUUID)):
                                        sourcesString += "," + uploadFileUUID[rsc]
                                        
                                    payload[data["data"][lineIndex]["params"][payIndex]["name"]] = sourcesString
                                
                                if len(uploadFileUUID)==1:
                                    payload[data["data"][lineIndex]["params"][payIndex]["name"]] = uploadFileUUID[0]
                                
                                if len(uploadFileUUID)==0:
                                    self.textEdit.append("No file resources found!")
                                    errorFlag =1
                                    
                        else:
                            payload[data["data"][lineIndex]["params"][payIndex]["name"]] = data["data"][lineIndex]["params"][payIndex]["value"]
                            
                            
                    
                    
                    if uploadedrscFlag != True:        
                        res = Response(requests.post(httpAddress + data["data"][lineIndex]["address"], data=payload, verify=False))
                        
                        if data["data"][lineIndex]["save"] == '1':
                            prevResponse = res.getJson()
                            prevPayload = payload
                        
                        if res.getStatus() == 200:
                            res.report_line(data["data"][lineIndex]['title'], self.textEdit)
                            
                            
                                    
                        else:
                            self.textEdit.append("Error: %d" % res.getStatus())
                            errorFlag = 1
                         
                    if len(data["data"][lineIndex]['find']) >= 1:
                            res.find(data["data"][lineIndex], lineIndex, errorFlag, self.textEdit)     
                         
                    if len(data["data"][lineIndex]['check']) >= 1:
                            res.check_value(data["data"][lineIndex], lineIndex, errorFlag, self.textEdit)
                                                   
                    
                #Delete line code
                if str.lower(data["data"][lineIndex]["method"]) == 'del': 
                    print("we have a deleter in line: " + str(lineIndex + 1))
                    
                
                if errorFlag == 1:
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