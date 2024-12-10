def Task01():
#Task 1:
# Write a function which take inputs(numbers) from user and prints its addition, multiplication, division and subtraction.

 a=input("enter num1: ")        
 b=input("enter num2: ")        
 calculator(a,b)

def calculator(num1,num2):
    print("Addition is : ",(int(num1)+int(num2)))
    print("Subtraction is : ",(int(num1)-int(num2)))
    print("Multiplication is : ",(int(num1)*int(num2)))
    if num2==0:
        print("diviion cannot be performed")
    else:
        print("Diviion  is : ",(int(num1)/int(num2)))

def Task02():
# Task 2:
# Write a program to calculatae the sum of all numbers in a given list using a for loop.
  Number_list=[4,5,3,64,9,2,14,43]
  Sum=0
  for index in range(len(Number_list)):
      Sum+=Number_list[index] 
  
  print("\n",Number_list,"\nSum of all numbers in above list is:",Sum)


def Task03():
   #Find the smallest number in a list:
   NumberList=[98,56,34,65,57,909,234,53,31,7]
   smallest=0
   for row in range(len(NumberList)):
      for col in range(row):
         if NumberList[row]<NumberList[col]:
            smallest=NumberList[row]
   print(smallest)

def Task04():
      for j in range(4):
         for k in range(j):
            print("*")
      print("Null")

def Task05():
  print("Null")

def TaskList():
   print("1.Task1\n2.Task2\n3.Task3\n4.Task4")    
   a=int(input("Enter num: "))
   if a==1:
      Task01()
   elif a==2:
      Task02()  
   elif a==3:
      Task03()  
   elif a==4:
      Task04()  
   elif a==5:
      Task05()
   else:
      print("Invalid Iput please select b\w 1 and 5")


TaskList()