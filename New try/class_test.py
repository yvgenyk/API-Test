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
        if self.responseStatus == 200:
            self.responseJson = self.r.json()
        else:
            self.responseJson = None
    
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
    def report_line(self, title, textEdit, method):
        textEdit.append(method + " Request \"" + title + "\":")
        textEdit.append(self.responseURL + "\n")
        textEdit.append("API response:")
        textEdit.append(self.responseText)
        textEdit.append("\n")
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    Find method, if there is a request to find something 
    in the response, this method will find it.
    """""""""""""""""""""""""""""""""""""""""""""""""""""
    def find(self,data, errorFlag, textEdit):
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
    def check_value(self, data, errorFlag, textEdit):
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
                print("\n\n" + str(prevResponse)+"\n\n")
                newAddress = addressCheck[:len(addressCheck)-4] + (str(prevResponse[0]["results"]))[2:(len(prevResponse[0]["results"])-3)]
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
                print("\n\nBeen here done that\n\n"+ res.getStatus() + "\n\n")
                prevResponse = res.responseJson()
                prevPayload = payload
                    
            if res.getStatus() == 200:
                res.report_line(self.testLine['title'], textEdit, "GET")
                    
                if len(self.testLine['find']) >= 1:
                    res.find(self.testLine, errorFlag, textEdit)
                
                if len(self.testLine['check']) >= 1:
                    res.check_value(self.testLine, errorFlag, textEdit)
                    
            else:
                print("\n\n\n get method 500\n\n")
                textEdit.append("Error: %d" % res.getStatus())
                errorFlag = 1
        
        
"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Post Method
                    
    This class is handling all the POST requests
                    
                    
"""""""""""""""""""""""""""""""""""""""""""""""""""
class PostMethod:
    
    def __init__(self, data):
            self.testLine = data
    
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    This is the main method, gets the line to execute and 
    sort between the types of requests.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def post_method(self, secretKey, publicKey, httpAddress, txtFilePath, txtFileUUID, testFilePath, uploadFileUUID, prevResponse, prevPayload, textEdit, errorFlag):
        payload = dict()
        uploadedrscFlag = [False]
        for payIndex in range(len(self.testLine['params'])):
                    
            if self.testLine["params"][payIndex] == "secret_key":
                payload[self.testLine["params"][payIndex]] = secretKey
                            
            elif self.testLine["params"][payIndex] == "public_key":
                payload[self.testLine["params"][payIndex]] = publicKey  
                
            #Text upload  
            elif self.testLine["params"][payIndex]["name"] == "textrsc":  
                self.text_upload(httpAddress, payIndex, payload, txtFilePath, textEdit, prevResponse, prevPayload, txtFileUUID, uploadedrscFlag, errorFlag)
                
            #File upload  
            elif self.testLine["params"][payIndex]["name"] == "filersc": 
                self.file_upload(httpAddress, payload, payIndex, testFilePath, textEdit, prevResponse, prevPayload, uploadFileUUID, uploadedrscFlag, errorFlag)
                
            #Use existing resources    
            elif self.testLine["params"][payIndex]["name"] == "sources":   
                self.ex_resource(payload, txtFileUUID, uploadFileUUID, textEdit, errorFlag)
                
            else:
                payload[self.testLine["params"][payIndex]["name"]] = self.testLine["params"][payIndex]["value"]
                
                        
        if uploadedrscFlag[0] == False:        
            res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False))
                
            if self.testLine["save"] == '1':
                prevResponse[0] = res.getJson()
                prevPayload = payload
                        
            if res.getStatus() == 200:
                res.report_line(self.testLine['title'], textEdit, "POST")
            else:
                    textEdit.append("Error: %d" % res.getStatus())
                    errorFlag = 1
             
                            
            if len(self.testLine['find']) >= 1:
                res.find(self.testLine, errorFlag, textEdit)     
                         
            if len(self.testLine['check']) >= 1:
                res.check_value(self.testLine, errorFlag, textEdit)
            
                
        
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
      This method will upload a free text resource from file.
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""    
    def text_upload(self, httpAddress, payIndex, payload, txtFilePath, textEdit, prevResponse, prevPayload, txtFileUUID, uploadedrscFlag, errorFlag):    
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
                            
            if len(txtFilePath) == 0:
                textEdit.append("No text file was added\n")
                                
            elif len(txtFilePath) >= 1:
                                
                for txtIndex in range(len(txtFilePath)):
                                
                    loadedFile = open(txtFilePath[txtIndex], 'r')
                                
                    with loadedFile:
                        txt = loadedFile.read()
                                    
                    payload['text'] = txt
                                        
                    res = Response(requests.post(httpAddress + self.testLine["address"], data=payload, verify=False))
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        prevPayload = payload
                                        
                    if res.getStatus() == 200:
                        res.report_line(self.testLine['title'], textEdit, "POST")
                                
                        uuidTxt = str(res.getJson()["results"])
                        txtFileUUID.append(uuidTxt[2:(len(uuidTxt)-2)])
                        uploadedrscFlag[0] = True 
                                            
                    else:
                        textEdit.append("Error: %d" % res.getStatus())
                        errorFlag = 1
        
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
            This method will upload a file resource
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def file_upload(self, httpAddress, payload, payIndex, testFilePath, textEdit, prevResponse, prevPayload, uploadFileUUID, uploadedrscFlag, errorFlag):   
        
        if self.testLine["params"][payIndex]["value"] == "empty":
            pass
        elif self.testLine["params"][payIndex]["value"] == "nokey":
            pass
                            
        else:
            if len(testFilePath) == 0:
                textEdit.append("No file was selected\n")
                                
            elif len(testFilePath) >= 1:
                                
                for fileIndex in range(len(testFilePath)):
                                
                    loadedFile = {'@upload': open(testFilePath[fileIndex], 'rb')}
                                        
                    res = Response(requests.post(httpAddress + self.testLine["address"], files = loadedFile, data = payload, verify=False))
                                        
                    if self.testLine["save"] == '1':
                        prevResponse[0] = res.getJson()
                        print("\n\nFile Uploaded" + str(prevResponse[0])+"\n\n")
                        prevPayload = payload
                                        
                    if res.getStatus() == 200:
                        res.report_line(self.testLine['title'], textEdit, "POST")
                                
                        uuidFile = str(res.getJson()["results"])
                        uploadFileUUID.append(uuidFile[2:(len(uuidFile)-2)])
                        uploadedrscFlag[0] = True 
                    
                    else:
                        textEdit.append("Error: %d" % res.getStatus())
                        errorFlag = 1     
    
     """""""""""""""""""""""""""""""""""""""""""""""""""""""""
     This method is for requests that need resource UUID to
     execute. The method will check which type of resource is
     needed (Text or File) and execute the request.
     """""""""""""""""""""""""""""""""""""""""""""""""""""""""
    def ex_resource(self, payload, txtFileUUID, uploadFileUUID, textEdit, errorFlag):   
        
        #Text sources
        if self.testLine["params"][payIndex]["value"] == "txt":
            sourcesString = ""
        if len(txtFileUUID)>1:
            for rsc in range(len(txtFileUUID)):
                sourcesString += "," + txtFileUUID[rsc]
                                        
                payload[self.testLine["params"][payIndex]["name"]] = sourcesString
                                    
        elif len(txtFileUUID)==1:
            payload[self.testLine["params"][payIndex]["name"]] = txtFileUUID[0]
                                
        elif len(txtFileUUID)==0:
            textEdit.append("No text resources found!")
            errorFlag =1
                                    
        #File sources
        else:
            sourcesString = ""
            if len(uploadFileUUID)>1:
                for rsc in range(len(uploadFileUUID)):
                    sourcesString += "," + uploadFileUUID[rsc]
                                        
                    payload[self.testLine["params"][payIndex]["name"]] = sourcesString
                                
            elif len(uploadFileUUID)==1:
                payload[self.testLine["params"][payIndex]["name"]] = uploadFileUUID[0]
                                
            elif len(uploadFileUUID)==0:
                textEdit.append("No file resources found!")
                errorFlag =1
    
        