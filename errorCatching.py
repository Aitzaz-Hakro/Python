# try:
#     number=int(input("enter a number "))
#     print("you entered: ",number)
#     print(number/0)
# except:
#     print("invalid input")    

try:
    number=int(input("enter a number "))
    print("you entered: ",number)

    print("want to divide with zero (y/n)")
    opt=input(": ")
    if opt=="y":
      number=number/0
    
except ZeroDivisionError :
    print("cannot  divided by zero")    
except ValueError as err: # exception as a variable
    print(err)    
    