#Initialising
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QSize
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

#Defining Global Variables
global spinval
global spinval2
global spinval3
global spinval4
global spinval5
global spinval6
global spinval7
global spinval8
global spinval9
global spinval10

#Each SpinVal represents the pricing of individual items
spinval = 2
spinval2 = 3
spinval3 = 4
spinval4 = 1
spinval5 = 1
spinval6 = 2
spinval7 = 3
spinval8 = 9
spinval9 = 10
spinval10 = 1

global finalval1
global finalval2
global finalval3
global finalval4
global finalval5
global finalval6
global finalval7
global finalval8
global finalval9
global finalval10

#FinalVal Represents the total cost of each individual item
finalval = 0
finalval2 = 0
finalval3 = 0
finalval4 = 0
finalval5 = 0
finalval6 = 0
finalval7 = 0
finalval8 = 0
finalval9 = 0
finalval10 = 0

global item1
global item2
global item3
global item4
global item5
global item6
global item7
global item8
global item9
global item10

#item represents the name of each individual item
item1 = ("Apple ($" + str(spinval)+")")
item2 = ("Milk ($" + str(spinval2)+")")
item3 = ("Carrot ($" + str(spinval3)+")")
item4 = ("Cracker ($" + str(spinval4)+")")
item5 = ("Radish ($" + str(spinval5)+")")
item6 = ("Flour ($" + str(spinval6)+")")
item7 = ("Sugar ($" + str(spinval7)+")")
item8 = ("Noodles ($" + str(spinval8)+")")
item9 = ("Rice ($" + str(spinval9)+")")
item10 = ("Orange ($" + str(spinval10)+")")


#Value is the overall cost
global value
value = 0

#Home Grown Grill Page 1
class HGGPage1(QDialog):
    #Initialising Window
    def __init__(self):
        super(HGGPage1, self).__init__()
        loadUi('internalproject1.ui', self)
        self.setWindowTitle('Home Grown Grill')
        self.nextButton.clicked.connect(self.on_nextButton_clicked)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.setMinimumSize(QSize(600, 300))
    @pyqtSlot()
    #When the 'Next' Button is Clicked
    def on_nextButton_clicked(self):
        #Calling Global Variables
        global finalfirstname
        global finallastname
        global finaladdress
        global finalphone_number

        #Creating Variables
        nameint = False
        last_nameint = False
        phone_numberstr = False

        #Creating Function
        def hasNumbers(inputString):
            return any(char.isdigit() for char in inputString)

        #Defining Variables
        name = self.lineEdit.text()
        name = name.lower().title().strip()
        finalfirstname = name
        #The variable finalfirstname is a global variable that is used in the final order evaluation (Page 4)

        last_name = self.lineEdit2.text()
        last_name = last_name.lower().title().strip()
        finallastname = last_name
        #The variable finallastname is a global variable that is used in the final order evaluation (Page 4)

        address = self.lineEdit3.text()
        address = address.lower().title().strip()
        finaladdress = address
        #The variable finaladdress is a global variable that is used in the final order evaluation (Page 4)

        phone_number = self.lineEdit4.text()
        phone_number = phone_number.lower().title().strip()
        finalphone_number = phone_number
        phone_number = phone_number.replace(" ","")
        #The variable finalphone_number is a global variable that is used in the final order evaluation (Page 4)

        #Check Validity of User Input

        if hasNumbers(name) == True:
            nameint = True

        if hasNumbers(last_name) == True:
            last_nameint = True

        try:
            phone_number = int(phone_number)
        except ValueError:
            phone_numberstr = True

        #If all inputs are filled continue to next window
        if name != "" and last_name != "" and address != "" and phone_number != "" and nameint == False and last_nameint == False and phone_numberstr == False:
            self.widget = HGGPage2()
            self.widget.show()
            self.hide()

        #If name has no input, display message
        if name == "" or nameint == True:
            if nameint == True:
                self.label5.setText("Your name must not contain numbers!")
            else:
                self.label5.setText("Please enter a name!")

        #If last_name has no input, display message
        if last_name == "" or last_nameint == True:
            if last_nameint == True:
                self.label6.setText("Your last name must not contain numbers!")
            else:
                self.label6.setText("Please enter a last name!")

        #If address has no input, display message
        if address == "":
            self.label7.setText("Please enter an address!")

        #If phone_number has no input, display message
        if phone_number == "" or phone_numberstr == True:
            if phone_number != "" and phone_numberstr == True:
                self.label8.setText("Your phone number must not contain letters!")
            else:
                self.label8.setText("Please enter a phone number!")


        #If name has input, remove message
        if name != "" and nameint == False:
            self.label5.setText("")

        #If last_name has input, remove message
        if last_name != "" and last_nameint == False:
            self.label6.setText("")

        #If address has input, remove message
        if address != "":
            self.label7.setText("")

        #If phone_number has input, remove message
        if phone_number != "" and phone_numberstr == False:
            self.label8.setText("")

    #If the Close Button is Clicked
    def on_pushButton_clicked(self):
        sys.exit(app.exec_())


#Home Grown Grill Page 2
class HGGPage2(QDialog):
    #Initalising Window
    def __init__(self):
        global item1
        global item2
        global item3
        global item4
        global item5
        global item6
        global item7
        global item8
        global item9
        global item10
        super(HGGPage2,self).__init__()
        loadUi('internalproject2.ui',self)
        self.setWindowTitle('Home Grown Grill')
        self.backButton.clicked.connect(self.on_backButton_clicked)
        self.nextButton.clicked.connect(self.on_nextButton_clicked)
        self.closeButton.clicked.connect(self.on_closeButton_clicked)
        self.setMinimumSize(QSize(600, 300))

        #Initialising Spinbox's
        #spinBox (#1)
        self.label_2.setText(item1)
        self.spinBox.valueChanged.connect(self.valuechange)
        self.spinBox.setMaximum(9)
        self.spinBox.setMinimum(0)

        #spinBox (#2)
        self.label_3.setText(item2)
        self.spinBox2.valueChanged.connect(self.valuechange2)
        self.spinBox2.setMaximum(9)
        self.spinBox2.setMinimum(0)

        #spinBox (#3)
        self.label_4.setText(item3)
        self.spinBox3.valueChanged.connect(self.valuechange3)
        self.spinBox3.setMaximum(9)
        self.spinBox3.setMinimum(0)

        #spinBox (#4)
        self.label_5.setText(item4)
        self.spinBox4.valueChanged.connect(self.valuechange4)
        self.spinBox4.setMaximum(9)
        self.spinBox4.setMinimum(0)

        #spinBox (#5)
        self.label_6.setText(item5)
        self.spinBox5.valueChanged.connect(self.valuechange5)
        self.spinBox5.setMaximum(9)
        self.spinBox5.setMinimum(0)

        #spinBox (#6)
        self.label_7.setText(item6)
        self.spinBox6.valueChanged.connect(self.valuechange6)
        self.spinBox6.setMaximum(9)
        self.spinBox6.setMinimum(0)

        #spinBox (#7)
        self.label_8.setText(item7)
        self.spinBox7.valueChanged.connect(self.valuechange7)
        self.spinBox7.setMaximum(9)
        self.spinBox7.setMinimum(0)

        #spinBox (#8)
        self.label_9.setText(item8)
        self.spinBox8.valueChanged.connect(self.valuechange8)
        self.spinBox8.setMaximum(9)
        self.spinBox8.setMinimum(0)

        #spinBox (#9)
        self.label_10.setText(item9)
        self.spinBox9.valueChanged.connect(self.valuechange9)
        self.spinBox9.setMaximum(9)
        self.spinBox9.setMinimum(0)

        #spinBox (#10)
        self.label_11.setText(item10)
        self.spinBox10.valueChanged.connect(self.valuechange10)
        self.spinBox10.setMaximum(9)
        self.spinBox10.setMinimum(0)

        #total cost
        self.spinBox.valueChanged.connect(self.totalcost)
        self.spinBox2.valueChanged.connect(self.totalcost)
        self.spinBox3.valueChanged.connect(self.totalcost)
        self.spinBox4.valueChanged.connect(self.totalcost)
        self.spinBox5.valueChanged.connect(self.totalcost)
        self.spinBox6.valueChanged.connect(self.totalcost)
        self.spinBox7.valueChanged.connect(self.totalcost)
        self.spinBox8.valueChanged.connect(self.totalcost)
        self.spinBox9.valueChanged.connect(self.totalcost)
        self.spinBox10.valueChanged.connect(self.totalcost)


    #When Next Button is Clicked
    def on_nextButton_clicked(self):
        if value > 0:
            self.widget = HGGPage3()
            self.widget.show()
            self.hide()
        else:
            self.label12.setText("You must make a purchase")

    #When Back Button is Clicked
    def on_backButton_clicked(self):
        self.widget = HGGPage1()
        self.widget.show()
        self.hide()

    #When Close Button is Clicked
    def on_closeButton_clicked(self):
        sys.exit(app.exec_())


    #Checking Spinbox Values
    #For each spin box, the spinbox value is assigned to a non global variable 'value' which is then displayed.
    #spinBox (#1)
    def valuechange(self):
        global spinval
        value = self.spinBox.value()
        value = value * spinval
        self.label.setText("Price: $"+ str(value))

    #spinBox (#2)
    def valuechange2(self):
        global spinval2
        value = self.spinBox2.value()
        value = value * spinval2
        self.label2.setText("Price: $"+ str(value))

    #spinBox (#3)
    def valuechange3(self):
        global spinval3
        value = self.spinBox3.value()
        value = value * spinval3
        self.label3.setText("Price: $"+ str(value))

    #spinBox (#4)
    def valuechange4(self):
        global spinval4
        value = self.spinBox4.value()
        value = value * spinval4
        self.label4.setText("Price: $"+ str(value))

    #spinBox (#5)
    def valuechange5(self):
        global spinval5
        value = self.spinBox5.value()
        value = value * spinval5
        self.label5.setText("Price: $"+ str(value))

    #spinBox (#6)
    def valuechange6(self):
        global spinval6
        value = self.spinBox6.value()
        value = value * spinval6
        self.label6.setText("Price: $"+ str(value))

    #spinBox (#7)
    def valuechange7(self):
        global spinval7
        value = self.spinBox7.value()
        value = value * spinval7
        self.label7.setText("Price: $"+ str(value))

    #spinBox (#8)
    def valuechange8(self):
        global spinval8
        value = self.spinBox8.value()
        value = value * spinval8
        self.label8.setText("Price: $"+ str(value))

    #spinBox (#9)
    def valuechange9(self):
        global spinval9
        value = self.spinBox9.value()
        value = value * spinval9
        self.label9.setText("Price: $"+ str(value))

    #spinBox (#10)
    def valuechange10(self):
        global spinval10
        value = self.spinBox10.value()
        value = value * spinval10
        self.label10.setText("Price: $"+ str(value))

    #Calculating total cost
    def totalcost(self):
        global spinval
        global spinval2
        global spinval3
        global spinval4
        global spinval5
        global spinval6
        global spinval7
        global spinval8
        global spinval9
        global spinval10
        global value
        #global item_amount
        #item_amount = self.spinBox.value() + self.spinBox2.value() + self.spinBox3.value() + self.spinBox4.value() + self.spinBox5.value() + self.spinBox6.value() + self.spinBox7.value() + self.spinBox8.value() + self.spinBox9.value() + self.spinBox10.value()
        #Value is calculated by adding every individual spinbox and multiplying it by it's designated spinval to come up with a total cost
        value = self.spinBox.value() * spinval  + self.spinBox2.value() * spinval2 + self.spinBox3.value() * spinval3 + self.spinBox4.value() * spinval4 + self.spinBox5.value() * spinval5 + self.spinBox6.value() * spinval6 + self.spinBox7.value() * spinval7 + self.spinBox8.value() * spinval8 + self.spinBox9.value() * spinval9 + self.spinBox10.value() * spinval10
        self.label11.setText("Total Cost: $"+ str(value))

#Home Grown Grill Page 3
class HGGPage3(QDialog):
    #Initialising
    def __init__(self):
        super(HGGPage3,self).__init__()
        loadUi('internalproject3.ui',self)
        self.setWindowTitle('Home Grown Grill')
        self.backButton.clicked.connect(self.on_backButton_clicked)
        self.closeButton.clicked.connect(self.on_closeButton_clicked)
        self.nextButton.clicked.connect(self.on_nextButton_clicked)
        self.setMinimumSize(QSize(687, 300))

    #When Back Button is Clicked
    def on_backButton_clicked(self):
        #The total value is set back to 0$
        global value
        value = 0
        self.widget = HGGPage2()
        self.widget.show()
        self.hide()

    #When Close Button is Clicked
    def on_closeButton_clicked(self):
        sys.exit(app.exec_())

    #When Next Button is Clicked
    def on_nextButton_clicked(self):
        #Checking Which Checkboxes are Checked
        #Checkbox #1
        if self.checkBox.isChecked():
            checkbox_1 = True
        else:
            checkbox_1 = False

        #Checkbox #2
        if self.checkBox_2.isChecked():
            checkbox_2 = True
        else:
            checkbox_2 = False

        #cost_after_paper is a variable that is set equal to the final 'value' plus one, this is used in the final cost summary
        if self.checkBox.isChecked() and checkbox_2 == False:
            global cost_after_paper
            global value
            cost_after_paper = value + 1
            if cost_after_paper == value + 1:
                cost_after_paper = cost_after_paper - 1
            self.widget = HGGPage4()
            self.widget.show()
            self.hide()
        elif self.checkBox_2.isChecked() and checkbox_1 == False:
            cost_after_paper = value + 1
            self.widget = HGGPage4()
            self.widget.show()
            self.hide()
        elif checkbox_1 == True and checkbox_2 == True:
            self.label_11.setText("Please Make One Selection")
        else:
            self.label_11.setText("Please Make A Selection")
#Home Grown Grill Page 4
class HGGPage4(QDialog):
    #Calling Global Variables
    global cost_after_paper
    #Initialising
    def __init__(self):
        super(HGGPage4,self).__init__()
        loadUi('internalproject4.ui',self)
        self.setWindowTitle('Home Grown Grill')
        self.setMinimumSize(QSize(687, 300))
        self.backButton.clicked.connect(self.on_backButton_clicked)
        self.closeButton.clicked.connect(self.on_closeButton_clicked)
        self.finishButton.clicked.connect(self.on_finishButton_clicked)
        #Displaying Values
        self.label_2.setText("Full Name: " + str(finalfirstname) + " " + str(finallastname))
        self.label_3.setText("Total Value: $" + str(cost_after_paper))
        self.label_4.setText("Address: " + str(finaladdress))
        self.label_5.setText("Phone Number: " + str(finalphone_number))

    #When Back Button is Clicked
    def on_backButton_clicked(self):
        self.widget = HGGPage3()
        self.widget.show()
        self.hide()

    #When Close Button is Clicked
    def on_closeButton_clicked(self):
        sys.exit(app.exec_())

    #When Finish Button is Clicked
    def on_finishButton_clicked(self):
        sys.exit(app.exec_())

app=QApplication(sys.argv)
widget=HGGPage1()
widget.show()
sys.exit(app.exec())
