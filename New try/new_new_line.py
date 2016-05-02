from PyQt4 import QtGui, QtCore
import new_line


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
        
        #prepare to write
        loadedFile = open(nameOfFile, 'w')
        
        line = (',{\"method\":\"' + self.newMethod.text() + '\",\"address\":\"' + self.newAddress.text() + '\",\"title\":\"' + 
                self.newTitle.text()) 
        
        if self.saveForNext.isChecked():
            line += ('\",\"save\":\"1\",\"params\":[\"' + self.sKey.text() + '\",\"' + self.pKey.text() + '\"]}')
        else:
            line += ('\",\"save\":\"0\",\"params\":[\"' + self.sKey.text() + '\",\"' + self.pKey.text() + '\"]}')
                   
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
        else:
            line = (line[:len(line)-1] + ',\"find\":[]' + line[len(line)-1:])
                
                
        
        if self.check_one_name.text() != '':        
            if self.checkPrevValue_1.isChecked():
                line = (line[:len(line)-1] + ',\"check\":[\"prev\",\"' + self.check_one_name.text() + '\"]' + line[len(line)-1:])
        
            else:         
                line = (line[:len(line)-1] + ',\"check\":[\"' + self.check_one_name.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_name.text() != '':
                if self.checkPrevValue_2.isChecked():
                    line = (line[:len(line)-2] + ',\"prev\",\"' + self.check_two_name.text() + '\"' + line[len(line)-2:])
                else:    
                    line = (line[:len(line)-2] + ',\"' + self.check_two_name.text() + '\"' + line[len(line)-2:])
                
            if self.check_three_name.text() != '':
                if self.checkPrevValue_3.isChecked():
                    line = (line[:len(line)-2] + ',\"prev\",\"' + self.check_three_name.text() + '\"' + line[len(line)-2:])
                else:
                    line = (line[:len(line)-2] + ',\"' + self.check_three_name.text() + '\"' + line[len(line)-2:])
        else:
             line = (line[:len(line)-1] + ',\"check\":[]' + line[len(line)-1:])
                    
        
        if self.check_one_value.text() != '':            
            line = (line[:len(line)-1] + ',\"value\":[\"' + self.check_one_value.text() + '\"]' + line[len(line)-1:])
            
            if self.check_two_value.text() != '':
                line = (line[:len(line)-2] + ',\"' + self.check_two_value.text() + '\"' + line[len(line)-2:])
                
                if self.check_three_value.text() != '':
                    line = (line[:len(line)-2] + ',\"' + self.check_three_value.text() + '\"' + line[len(line)-2:])
        else:
            line = (line[:len(line)-1] + ',\"value\":[]' + line[len(line)-1:])

        
        #find the place where to add the new line
        fileEnd = len(text)-2
        
        #create new text
        newText = text[:fileEnd] + line + text[fileEnd:]
        
        #overwrite the existing file with new content
        loadedFile.write(newText)
        loadedFile.close()