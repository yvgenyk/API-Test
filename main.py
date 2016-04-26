from PyQt4 import QtGui, QtCore
import sys
import design
import jsoncreator
import new_line
import requests
import re
import json
import time
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
        
        
        self.json_work = None
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
        
        if (testFile):
            startFlag = 1
        else:
            choice = QtGui.QMessageBox.question(self, 'No File', "No file was loaded, would you like to load?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        
            if choice == QtGui.QMessageBox.Yes:
                self.json_work = JsonCreator()
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
            
            
            with open(testFile) as codeLines_data:
                data = json.load(codeLines_data)
            for lineIndex in range(len(data["data"])):  
                
                
                
                #Get line code
                if data["data"][lineIndex]["method"] == 'get' or data["data"][lineIndex]["method"] == 'GET':
                    #payload initialization
                    payload = dict()
                    for payIndex in range(len(data["data"][lineIndex]['params'])):
                    
                        if data["data"][lineIndex]["params"][payIndex] == "secret_key":
                            payload[data["data"][lineIndex]["params"][payIndex]] = secretKey
                            
                        elif data["data"][lineIndex]["params"][payIndex] == "public_key":
                            payload[data["data"][lineIndex]["params"][payIndex]] = publicKey
                            
                        else:
                            payload[data["data"][lineIndex]["params"][payIndex]['name']] = data["data"][lineIndex]["params"][payIndex]['value']
                            
                            
                    r = requests.get(httpAddress + data["data"][lineIndex]["address"], params=payload, verify=False)
                    
                    if r.status_code == 200:
                        self.textEdit.append("GET Request \"" + data["data"][lineIndex]['title'] + "\":")
                        self.textEdit.append(r.url + "\n")
                        self.textEdit.append("API response:")
                        self.textEdit.append(r.text)
                        self.textEdit.append("\n")
                    
                        if len(data["data"][lineIndex]['find']) >= 1:
                            for findIndex in range(len(data["data"][lineIndex]['find'])):
                                if data["data"][lineIndex]['find'][findIndex] in r.text:
                                    pass
                                else:
                                    self.textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]['find'][findIndex] + " wasn't found in :\n" + r.text)
                                    errorFlag = 1
                    
                        if len(data["data"][lineIndex]['check']) >= 1:
                            for checkIndex in range(len(data["data"][lineIndex]['check'])):
                                varToCheck = data["data"][lineIndex]["check"][checkIndex]
                           
                                if data["data"][lineIndex]['value'][checkIndex] == str(r.json()["status"][varToCheck]):
                                    pass
                                else:
                                    self.textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]["check"][checkIndex] + 
                                                         ": " + data["data"][lineIndex]["value"][checkIndex] + " wasn't found in :\n" + r.text)
                                    errorFlag = 1
                    
                    else:
                        self.textEdit.append("Error: %d" % r.status_code)
                        errorFlag == 1
                    
                    
                    
                    
                    
                    
                    
                    
                #Post line code
                if data["data"][lineIndex]["method"] == 'post' or data["data"][lineIndex]["method"] == 'POST': 
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
                                
                                        r = requests.post(httpAddress + data["data"][lineIndex]["address"], data=payload, verify=False)
                                        if r.status_code == 200:
                                            self.textEdit.append("POST Request \"" + data["data"][lineIndex]['title'] + "\":")
                                            self.textEdit.append(r.url + "\n")
                                            self.textEdit.append("API response:")
                                            self.textEdit.append(r.text)
                                            self.textEdit.append("\n")
                                
                                            uuidTxt = str(r.json()["results"])
                                            txtFileUUID.append(uuidTxt[2:(len(uuidTxt)-2)])
                                            uploadedrscFlag = True
                                            
                                        else:
                                            self.textEdit.append("Error: %d" % r.status_code)
                                            errorFlag == 1
                            
                        
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
                                
                                        r = requests.post(httpAddress + data["data"][lineIndex]["address"], files = loadedFile, data = payload, verify=False)
                                        if r.status_code == 200:
                                            self.textEdit.append("POST Request \"" + data["data"][lineIndex]['title'] + "\":")
                                            self.textEdit.append(r.url + "\n")
                                            self.textEdit.append("API response:")
                                            self.textEdit.append(r.text)
                                            self.textEdit.append("\n")
                                
                                            uuidFile = str(r.json()["results"])
                                            uploadFileUUID.append(uuidFile[2:(len(uuidFile)-2)])
                                            uploadedrscFlag = True
                    
                                        else:
                                            self.textEdit.append("Error: %d" % r.status_code)
                                            errorFlag == 1
                 
                        
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
                        r = requests.post(httpAddress + data["data"][lineIndex]["address"], data=payload, verify=False)
                        if r.status_code == 200:
                            self.textEdit.append("POST Request \"" + data["data"][lineIndex]['title'] + "\":")
                            self.textEdit.append(r.url + "\n")
                            self.textEdit.append("API response:")
                            self.textEdit.append(r.text)
                            self.textEdit.append("\n")
                            
                            
                                    
                        else:
                            self.textEdit.append("Error: %d" % r.status_code)
                            errorFlag == 1
                         
                         
                         
                    if len(data["data"][lineIndex]['find']) >= 1:
                        for findIndex in range(len(data["data"][lineIndex]['find'])):
                            if data["data"][lineIndex]['find'][findIndex] in r.text:
                                pass
                            else:
                                self.textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]['find'][findIndex] + " wasn't found in :\n" + r.text)
                                errorFlag = 1
                    
                    if len(data["data"][lineIndex]['check']) >= 1:
                        for checkIndex in range(len(data["data"][lineIndex]['check'])):
                            varToCheck = data["data"][lineIndex]["check"][checkIndex]
                           
                            if data["data"][lineIndex]['value'][checkIndex] == str(r.json()["status"][varToCheck]):
                                pass
                            else:
                                self.textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]["check"][checkIndex] + 
                                                    ": " + data["data"][lineIndex]["value"][checkIndex] + " wasn't found in :\n" + r.text)
                                errorFlag = 1
                                    
                                       
                    
                #Delete line code
                if data["data"][lineIndex]["method"] == 'del': 
                    print("we have a deleter in line: " + str(lineIndex + 1))
                    
                
                if errorFlag == 1:
                    break
    
                self.progressBar.setValue((100/(len(data["data"]))*(lineIndex+1)))
                time.sleep(0.5)

        
        
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
        
        
        
    def close_window(self):
        self.close()
        
    def load_file(self):
        global testFile
        testFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(testFile, 'r')
        
        with loadedFile:
            text = loadedFile.read()
            
            textSplit = text.split('oid')
            index = len(textSplit)
            self.textEditFileLoad.setText(text)
        
            
    def new_file(self):
        self.textEditFileLoad.setText('{"data":[{"method":"<GET/POST/DELETE>","address":"<spesific address>","title":"<name of the test>"' + 
        ',"params":[' +
        '"secret_key",' +
        '"public_key",' +
        '{"name":"<any param to send>","value":"<any param value>"}],' +
        '"find":[],"check":[],"value":[]}]}')
        
    def save_file(self):
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '.json','*.json')
        file = open(fileName, 'w')
        text = self.textEditFileLoad.toPlainText()
        file.write(text)
        file.close()
        
        
    def edit_file(self):
        
        self.new_line_window = NewLine()
        self.new_line_window.show()
        self.textEditFileLoad.setText(',{"method":"<GET/POST/DELETE>","address":"<spesific address>","title":"<name of the test>"' + 
        ',"params":[' +
        '"secret_key",' +
        '"public_key",' +
        '{"name":"<any param to send>","value":"<any param value>"}],' +
        '"find":[],"check":[],"value":[]}')
        
        
        
class NewLine(QtGui.QMainWindow, new_line.Ui_NewLine):
    def __init__(self, parent=None):
        super(NewLine, self).__init__(parent)
        self.setupUi(self)
        self.new_line_window = None
        
        self.saveBtn.clicked.connect(self.saveNewLine_file)
        self.closeBtn.clicked.connect(self.close_window)
        self.sKey.setText('secret_key')
        self.pKey.setText('public_key')
        
        
        
    def close_window(self):
        self.close()
        
        
    def saveNewLine_file(self):
        
        #read the file
        nameOfFile = QtGui.QFileDialog.getOpenFileName(self, 'Open File', "*.json")
        loadedFile = open(nameOfFile, 'r')
        
        #convert to text
        with loadedFile:
            text = loadedFile.read()
            
        #find index number
        #textSplit = text.split('oid')
        #newIndex = len(textSplit)
        
        #prepare to write
        loadedFile = open(nameOfFile, 'w')
        
        line = (',{\"method\":\"' + self.newMethod.text() + '\",\"address\":\"' + self.newAddress.text() + '\",\"title\":\"' + 
                self.newTitle.text() + '\",\"params\":[\"' + self.sKey.text() + '\",\"' + self.pKey.text() + '\"]}')
                
        if self.p_one_name.text() != '':
            line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_one_name.text() + '\",\"value\":\"' + self.p_one_value.text() + '\"}' + line[len(line)-2:])
                
            if self.p_two_name.text() != '':
                line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_two_name.text() + '\",\"value\":\"' + self.p_two_value.text() + '\"}' + line[len(line)-2:])   
                    
                if self.p_three_name.text() != '':
                    line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_three_name.text() + '\",\"value\":\"' + self.p_three_value.text() + '\"}' + line[len(line)-2:])
                
                    if self.p_four_name.text() != '':
                        line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_four_name.text() + '\",\"value\":\"' + self.p_four_value.text() + '\"}' + line[len(line)-2:])
                
                        if self.p_five_name.text() != '':
                            line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_five_name.text() + '\",\"value\":\"' + self.p_five_value.text() + '\"}' + line[len(line)-2:])
                
                            if self.p_six_name.text() != '':
                                line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_six_name.text() + '\",\"value\":\"' + self.p_six_value.text() + '\"}'  + line[len(line)-2:])  
                      
                                if self.p_seven_name.text() != '':
                                    line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_seven_name.text() + '\",\"value\":\"' + self.p_seven_value.text() + '\"}' + line[len(line)-2:])
                
                                    if self.p_eight_name.text() != '':
                                        line = (line[:len(line)-2] + ',{\"name\":\"' + self.p_eight_name.text() + '\",\"value\":\"' + self.p_eight_value.text() + '\"}' + line[len(line)-2:])          
            
        
        if self.findOne.text() != '':
            line = (line[:len(line)-1] + ',\"find\":[\"' + self.findOne.text() + '\"]' + line[len(line)-1:])
            
            if self.findTwo.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.findTwo.text() + '\"' + line[len(line)-2:])
                
                if self.findThree.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.findThree.text() + '\"' + line[len(line)-2:])
                
                 
        if self.check_one_name.text() != '':
            line = (line[:len(line)-1] + ',\"check\":[\"' + self.check_one_name.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_name.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.check_two_name.text() + '\"' + line[len(line)-2:])
                
                if self.check_three_name.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.check_three_name.text() + '\"' + line[len(line)-2:])
                    
                    
        if self.check_one_value.text() != '':
            line = (line[:len(line)-1] + ',\"value\":[\"' + self.check_one_value.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_value.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.check_two_value.text() + '\"' + line[len(line)-2:])
                
                if self.check_three_value.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.check_three_value.text() + '\"' + line[len(line)-2:])
            

        
        #find the place where to add the new line
        fileEnd = len(text)-2
        
        #create new text
        newText = text[:fileEnd] + line + text[fileEnd:]
        
        #overwrite the existing file with new content
        loadedFile.write(newText)
        loadedFile.close()
        
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    form = TestApp()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()