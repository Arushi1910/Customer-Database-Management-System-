#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pickle
import os
import sys
class bank:
    BankName="State Bank of India"
    def __init__(self):
        self.owner=""
        self.phone=0
        self.accountno=0
        self.currba=0
        self.acctype=""
        
    def inputdet(self):
        self.owner=input("Enter Name of the Account Owner: ")
        self.phone=int(input("Enter 10 digit Phone number: "))
        while(len(str(self.phone))!=10):
            self.phone=int(input("Please Enter valid 10 digit Phone number: "))
        self.accountno=int(input("Enter 7 Digit Account Number of the user: "))
        while(len(str(self.accountno))!=7):
            self.accountno=int(input("Please Enter valid 7 digit Account number: "))
        self.currba=int(input("Enter Current balance of the account: "))
        while(self.currba<1000):
            self.currba=int(input("Minimum Account Balance should be Rs.1000: "))
        self.acctype=input("Enter Account Type Savings(S) or Current(C): ")
        while(self.acctype not in'S' and self.acctype not in'C'):
            self.acctype=input("Please enter valid Account Type Savings(S) or Current(C): ")
        print("")
    
    def modify(self):
        ch="Y"
        while(ch=="Y"):
            print("Select the detail you want to modify:\nPress 1: To modify the Name \nPress 2: To modify Phone Number \nPress 3: To modify the Account Type ")
            n=int(input(""))
            print(115*"*")
            while(n<=0 or n>4):
                print("Please enter a valid choice ")
                n=int(input(""))
            if (n==1):
                self.owner=input("Enter Full Name of the Account Owner: ")
            if (n==2):
                self.phone=int(input("Enter 10 digit Phone number: "))
                while(len(str(self.phone))!=10):
                    self.phone=int(input("Please Enter valid 10 digit Phone number: "))
            if (n==3):
                self.acctype=input("Enter Account Type Savings(S) or Current(C): ")
                while(self.acctype not in'S' and self.acctype not in'C'):
                    self.acctype=input("Please enter valid Account Type Savings(S) or Current(C): ")
            if (n==4):
                print("Updated Record is: ")
                
                break
            ch=input("If you wish to continue to modify the record Press Y else Press N:\n ")
            print ("Name of the Account Holder is: ",self.owner)
            print ("Phone Number of the Account Holder is: ",self.phone)
            print ("Account Type of the Account Holder is: ",self.acctype)
            print(115*"*")
            if (ch!='Y'):
                print("Modification Completed")
        
    def deposit(self):
        amdep=int(input("Enter Amount Deposited by the user: "))
        self.currba=self.currba+amdep
        print ("Updated Balance is: ",self.currba)
        
    def withdraw(self):
        amwith=int(input("Enter amount to be Withdrawn by the user: "))
        if((self.currba-amwith)>1000):
            self.currba=self.currba-amwith
            print ("Updated Balance is: ",self.currba)
        else:
            print("Mininimum Balance required is Rs.1000 hence you cannot withdraw cash")
            
    def display(self):
        print ("Name of the Account Holder is: ",self.owner)
        print ("Phone Number of the Account Holder is: ",self.phone)
        print ("Account Number of the Account Holder is: ",self.accountno)
        print ("Current Balance of the Account Holder is: ",self.currba)
        print ("Account Type of the Account Holder is: ",self.acctype)
        print("")
        
    def getaccno(self):
        return self.accountno
#main
def addrecord():
    try:
        file=open("Bank.dat","ab")
        b1=bank()
        b1.inputdet()
        pickle.dump(b1,file)
        file.close()
    except:
        pass
    
def searchrecord():
    file=open("Bank.dat","rb")
    acc=int(input("Enter Account Number to searched: "))
    c=0
    try:
        while(True):
            b2=pickle.load(file)
            if(b2.accountno==acc):
                b2.display()
                c=1
                break
    except:
        pass
    if(c!=1):
        print("Record NOT FOUND")
    file.close()
    
def deleterecord():
    file=open("Bank.dat","rb")
    yourfile=open("temp.dat","wb")
    rec=int(input("Enter the record number you want to delete: "))
    count=0
    c=0
    try:
        while (True):
            ob1=pickle.load(file)
            count=count+1
            if (count!=rec):
                pickle.dump(ob1,yourfile)
    except EOFError:
        pass
    file.close()
    yourfile.close()
    os.remove("Bank.dat")
    os.rename("temp.dat","Bank.dat") 
    print("Updated File Reecord is:")
    displayfile()
    
def modifyrecord():

    accno=int(input("Enter account number to be modified: "))
    c=0
    try:
        file=open("Bank.dat","rb")
        myfile=open("temp.dat","wb")
        while(True):
            b1=pickle.load(file)
            if(b1.getaccno()==accno):
                b1.display()
                b1.modify()
                pickle.dump(b1,myfile)
                c=1
                print("Record Updated ")
                break
            else:
                pickle.dump(b1,myfile)        
    except EOFError:
        pass
    if(c!=1):
        print("Record not found !")
    file.close() 
    myfile.close()
    os.remove("Bank.dat")
    os.rename("temp.dat","Bank.dat")

def displayfile():
    file=open("Bank.dat","rb")
    try:
        c=1
        while(True):
            ob1=pickle.load(file)
            print("Record Number: ",c)
            ob1.display()
            c=c+1
            print(100*"*")
    except EOFError:
        pass
    file.close()
    
def depositamt():
    c=0
    try:
        file=open("Bank.dat","rb")
        myfile=open("temp.dat","wb")
        accno=int(input("Enter the Account Number to Deposit the amount: "))
        while(True):
            b1=pickle.load(file)
            if(b1.getaccno()==accno):
                b1.display()
                b1.deposit()
                pickle.dump(b1,myfile)
                c=1
                break
            else:
                
                pickle.dump(b1,myfile)
    except:
        pass
    if(c!=1):
        print("Wrong Account Number")
    file.close()
    myfile.close()
    os.remove("Bank.dat")
    os.rename("temp.dat","Bank.dat")

def withamt():  
    c=0
    try:
        file=open("Bank.dat","rb")
        myfile=open("temp.dat","wb")
        accno=int(input("Enter the Account Number to Withdarw the amount: "))
        while(True):
            b1=pickle.load(file)
            if(b1.getaccno()==accno):
                b1.display()
                b1.withdraw()
                pickle.dump(b1,myfile)
                c=1
                break
            else:
                
                pickle.dump(b1,myfile)
    except:
        pass
    if(c!=1):
        print("Wrong Account Number")
    file.close()
    myfile.close()
    os.remove("Bank.dat")
    os.rename("temp.dat","Bank.dat")
            
#Menu
print("\t\t\t\t Welcome to State Bank of India Banking System ")
print(115*"*")
ch="Y"
while(ch=="Y"):
    print("Select the operation you want to perform:\nPress 1: To Add a record \nPress 2: To Search a record \nPress 3: To Delete a record \nPress 4: To Modify a record \nPress 5: To Display the records \nPress 6: To Withdraw Amount \nPress 7: To Deposit Amount \nPress 8: To Exit ")
    n=int(input(""))
    print(115*"*")
    while(n<=0 or n>8):
        print("Please enter a valid choice ")
        n=int(input(""))
    if (n==1):
        addrecord()
    if (n==2):
        searchrecord()
    if (n==3):
        deleterecord()
    if (n==4):
        modifyrecord()
    if (n==5):
        displayfile()
    if (n==6):
        withamt()
    if (n==7):
        depositamt()
    if (n==8):
        break
    ch=input("If you wish to continue Press Y else Press N:  ")
    print(115*"*")
    if (ch!='Y'):
        print("Thankyou! Have a Nice Day ")


# In[2]:



    c=0


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




