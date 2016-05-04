from PyQt4 import QtGui, QtCore
import design
import requests
import json
import time
import re
        
"""""""""""""""""""""""""""""""""""""""""""""
                    Response

This class is handeling the response after 
API call.


"""""""""""""""""""""""""""""""""""""""""""""        
class Response:
    """""""""""""""""""""""""""""""""
    Initializing the object with
    the basic thing for the program.
    """""""""""""""""""""""""""""""""
    def __init__(self, res):
        self.r = res
        self.responseURL = self.r.url
        self.responseStatus = self.r.status_code
        self.responseText = self.r.text
        self.responseJson = self.r.json()
    
    """""""""""""""""""""""""""
    Returns the requested URL.
    """""""""""""""""""""""""""
    def getURL(self):
        return self.responseURL
    
    """""""""""""""""""""""""""
    Return request status.
    """""""""""""""""""""""""""
    def getStatus(self):
        return self.responseStatus
    
    """""""""""""""""""""""""""
    Returns response as text.
    """""""""""""""""""""""""""
    def getText(self):
        return self.responseText
    """""""""""""""""""""""""""
    Returns response as JSON 
    format.
    """""""""""""""""""""""""""
    def getJson(self):
        return self.responseJson
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Prints the request and the response in the text editor
    of the program for later review.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def report_line(self, title, textEdit):
        textEdit.append("GET Request \"" + title + "\":")
        textEdit.append(self.responseURL + "\n")
        textEdit.append("API response:")
        textEdit.append(self.responseText)
        textEdit.append("\n")
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Find method, if there is a request to find something 
    in the response, this method will find it.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def find(self,data, lineIndex, errorFlag, textEdit):
        for findIndex in range(len(data['find'])):
            if data['find'][findIndex] in self.getText():
                pass
            else:
                textEdit.append("\n\n There was a problem: " + data['find'][findIndex] + " wasn't found in :\n" + self.getText())
                errorFlag = 1
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Check method, if there is certain values to check 
    in the response, this method will check them.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def check_value(self, data, lineIndex, errorFlag, textEdit):
        for valIndex in range(len(['value'])):
            #If this is true, the method will check the values with the values from last call/response.
            if data["check"][valIndex*2] == 'prev':
                varToCheck = data["check"][(valIndex*2 + 1)]
                
                if data['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["check"][(valIndex*2+1)] + 
                                    ": " + data["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag = 1
            #Else will check the provided values by the user against the response.                            
            else:
                varToCheck = data["check"][valIndex]
                                
                if data['value'][valIndex] == str(self.getJson()["results"][varToCheck]):
                    pass
                else:
                    textEdit.append("\n\n There was a problem: " + data["check"][valIndex] + 
                                    ": " + data["value"][valIndex] + " wasn't found in :\n" + self.getText())
                    errorFlag = 1
        
        
        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Get Method Class

    This class will handle all the get requests.


"""""""""""""""""""""""""""""""""""""""""""""""""""        
class GetMethod:
        
        def __init__(self, data):
            self.testLine = data
            
        """""""""""""""""""""""""""""""""
        The get method itself, will get
        everything it needs from the main 
        class and execute the request. 
        """""""""""""""""""""""""""""""""
        def get_method(self, secretKey, publicKey, httpAddress, errorFlag, prevResponse, prevPayload, textEdit, lineIndex):
            
            uuidToAddress = 0
            payload = dict()
            
            """""""""""""""""""""""""""""""""""""""""""""
            Collecting all the data from the instruction 
            file to execute the request.
            Including secret key, public key, address
            and any other data needed for the request
            """""""""""""""""""""""""""""""""""""""""""""
            for payIndex in range(len(self.testLine['params'])):
                    
                if self.testLine["params"][payIndex] == "secret_key":
                    payload[self.testLine["params"][payIndex]] = secretKey
                            
                elif self.testLine["params"][payIndex] == "public_key":
                    payload[self.testLine["params"][payIndex]] = publicKey
                            
                else:
                    payload[self.testLine["params"][payIndex]['name']] = self.testLine["params"][payIndex]['value']
                            
                            
            """""""""""""""""""""""""""""""""""""""""
            If an input from earlier request is 
            needed, like the resouce uuid, this code 
            will find the relevant uuid and create 
            the new address line.
            """""""""""""""""""""""""""""""""""""""""
            addressCheck = self.testLine["address"]
            if addressCheck[len(addressCheck)-4:] == 'uuid':
                newAddress = addressCheck[:len(addressCheck)-4] + (str(prevResponse["results"]))[2:(len(prevResponse["results"])-3)]
                uuidToAddress = 1
                        
            if uuidToAddress == 1:
                res = Response(requests.get(httpAddress + newAddress, params=payload, verify=False))
            else:
                res = Response(requests.get(httpAddress + self.testLine["address"], params=payload, verify=False))
            """""""""""""""""""""""""""""""""""""""""""""""
            If the save option is checked, will save the
            response and the request of the current request
            """""""""""""""""""""""""""""""""""""""""""""""           
            if self.testLine["save"] == '1':
                prevResponse = res.responseJson()
                prevPayload = payload
                    
            if res.getStatus() == 200:
                res.report_line(self.testLine['title'], textEdit)
                    
                if len(self.testLine['find']) >= 1:
                    res.find(self.testLine, lineIndex, errorFlag, textEdit)
                
                if len(self.testLine['check']) >= 1:
                    res.check_value(self.testLine, lineIndex, errorFlag, textEdit)
                    
            else:
                textEdit.append("Error: %d" % res.getStatus())
                errorFlag = 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        