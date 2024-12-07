from math import*

def calculator(a,b,stringg):
    if stringg==1:
        print(a+b)
    elif stringg==2:
        print(a-b)
    elif stringg==3:
        print(a*b)
    elif stringg==4:
        print(a/b)
    else:
       print("incorrect option")
       return

def menu():
    print("enter operation to perform \n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

a=int(input("enter number1: "))
b=int(input("enter number2: "))
menu()
oper=int(input("enter operation: "))
calculator(a,b,oper)