
# ismale=False
# a=input("enter gender ")

# if a=="male":
#     ismale=True    
# elif a=="female":
#     ismale= False
# else:
#     print("wrong Input")
# #################
# if ismale==True:
#     print("male")
# else:
#     print("female")

# tall=True
# if ismale and tall:
#     print("tall male")
# elif ismale and not(tall):
#     print("you are short male")
# else:
#     print("you are not a male")


#greatest among 3 numbers 
b=input("enter num1: ")
c=input("enter num2: ")
d=input("enter num3: ")

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        print("Num 1 is Greater")
    elif num2>=num1 and num2>=num3:
        print("Num 2 is Greater")
    else:
        print("Num 3 is Greater")

max_num(b,c,d)
