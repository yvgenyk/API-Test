from PyQt4 import QtGui, QtCore
import design
import requests
import json
import re

class ClassTest:
    name = ''
    
    def __init__(self, name):
        self.name = name
    
    def printSomething(self):
        print("\n\n%s\n\n" % self.name )
        
        
class Response:
    
    def __init__(self, r):
        self.responseURL = r.url
        self.responseStatus = r.status_code
        self.responseText = r.text
        self.responseJson = r.json()
        
    def getURL(self):
        return self.responseURL
    
    def getStatus(self):
        return self.responseStatus
    
    def getText(self):
        return self.responseText
    
    def getJson(self):
        return self.responseJson
        
    def report_line(self, title, textEdit):
        textEdit.append("GET Request \"" + title + "\":")
        textEdit.append(self.responseURL + "\n")
        textEdit.append("API response:")
        textEdit.append(self.responseText)
        textEdit.append("\n")
        
    def find(self, data, lineIndex, errorFlag, textEdit):
        for findIndex in range(len(data["data"][lineIndex]['find'])):
            if data["data"][lineIndex]['find'][findIndex] in self.getText():
                pass
            else:
                textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]['find'][findIndex] + " wasn't found in :\n" + self.getText())
                errorFlag = 1
        
    
    def check_value(self, data, lineIndex, errorFlag, textEdit):
        for valIndex in range(len(data["data"][lineIndex]['value'])):
            if data["data"][lineIndex]["check"][valIndex*2] == 'prev':
                varToCheck = data["data"][lineIndex]["check"][(valIndex*2 + 1)]
                
                if data["data"][lineIndex]['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]["check"][(valIndex*2+1)] + 
                                    ": " + data["data"][lineIndex]["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag = 1
                                        
            else:
                varToCheck = data["data"][lineIndex]["check"][valIndex]
                                
                if data["data"][lineIndex]['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["data"][lineIndex]["check"][valIndex] + 
                                    ": " + data["data"][lineIndex]["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag = 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        