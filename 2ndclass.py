#************tuples***********

coordinates= (4,5) #cannot be modified

lisst = [(4,5),(2,5)] #these tuples in list can be modified
print(coordinates[0]) #gives 4


#************ FUNCTIONS ****************

def add_num():
    print("numbers added") # press enter to indent 

add_num()   #function called
print("function called above") 


#parameterized functions 
def showname(name):
    print("hello " + name)

showname("Aitzaz")

def shownameandage(name):
    print("hello " + name)

showname("Aitzaz")

def cube(num):
    return num*num*num

print(cube(3))