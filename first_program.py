from math import*

print("hello world")
name="Aitzaz\nHassan" 
# print("before replace")
# print(name)
# print("After replace")
# print(name.upper().isupper())  gives true
# print(name.lower().isupper())  gives false

# print(name.replace("Aitzaz","Adeel"))


 # operations function
# a=4
# b=5
# c=-3
# print(sqrt(a)) #fron math function
# print( abs(c))
# print( max(a,b,c))
# print( min(a,b,c))
# print(round(a,b))
  
# age = input("Enter your age: ")
# print("your name: Aitzaz")
# print("yours age: " + age)



# num1=input("Enter Num1 ")
# num2=input("Enter Num2 ")
# result= int(num1) + int(num2)
# print(result)

array= ["Aitzaz","Hammad","Nabeel"]
num_list=[1,3,5,6,2,7]
print(array[1])
print(array[-3]) #start count from left 

array.extend(num_list) #JOIN TWO LISTS
print(array)

array.append("4554")
print(array)
array.insert(4,"232")
print(array)
array.remove("Nabeel")
print(array)
array.pop()
print(array)
# array.clear()  # clears the list
# print(array)

print(array.index("232"))
num_list.sort()
print(num_list)
