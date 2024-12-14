import os
CurrentBalance:float = 0.0
def MainMenu():
    os.system("cls") #clears the screen
    print("1.Check Balance\n2.Deposit Amount\n3.Withdraw Amount\n4.Exit")

def CheckBalance():
    print("Balance is: ",CurrentBalance)

print(CurrentBalance)
def Deposit():
     
     try:
       amount=int(input("Enter Amount to Deposit: "))
       if amount<=0:
          print("cannot Deposited!!")
       else:
          CurrentBalance+=amount
          print("Amount Deposited")
          

     except UnboundLocalError as err:
         print(err)
     except ValueError:
      print("Incorrect Input")

Deposit()
print(CurrentBalance)