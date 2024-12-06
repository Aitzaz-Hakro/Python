from math import*

def calculator(a,b,stringg):
    if stringg=="-":
        return a-b
    elif stringg=="+":
        return a+b
    elif stringg=="*":
        return a*b
    elif stringg=="/":
        return a/b
    else:
       print("incorrect option")
       return

def menu():
    print("")