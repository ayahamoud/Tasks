#!/usr/bin/env python
# coding: utf-8

# In[ ]:


inputNum = input('The list of numbers: ')
list_of_numbers = [int(item) for item in inputNum.split(',')]

#Check if the list contain up to 10 numbers and only positive numbers
while len(list_of_numbers)>10 or (not all(val > 0 for val in list_of_numbers)):
    if len(list_of_numbers)>10:
            print("The list can contain up to 10 numbers")
    else: 
        print("The list can contain only positive numbers")
    inputNum = input('The list of numbers: ')
    list_of_numbers = [int(item) for item in inputNum.split(',')]
    
print("The largest number in the list is :", max(list_of_numbers), 
      "\nThe smallest number in the list is :", min(list_of_numbers))


# In[ ]:


import pprint
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to your bank account")

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount,"\n")
        return amount

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount,"\n")
        else:
            print("\n Insufficient balance \n")
        return amount

    def check_Balance(self):
        print("\n Net Available Balance=",self.balance,"\n")
        return self.balance


s = Bank_Account()
i=1
history = {}
print("Please select the number of the action",
      "\n1- deposit \n2- withdraw \n3- check balance", 
      "\n4- display transaction history \n5- exit")
option = int(input(": "))
while option != 5:
    if option == 1:
        temp = s.deposit()
        history[i]=("Deposit",temp)
        i+=1
    elif option == 2:
        temp = s.withdraw()
        history[i]=("withdraw",temp)
        i+=1
    elif option == 3:
        temp = s.check_Balance()
        history[i]=("check balance",temp)
        i+=1
    elif option == 4:
        pprint.pprint(history)
    else: 
        print("Select valid option!")
    print("Please select the number of the action",
      "\n1- deposit \n2- withdraw \n3- check balance", 
      "\n4- display transaction history \n5- exit")
    option = int(input(": "))


