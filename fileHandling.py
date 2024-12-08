
# family = open("filee.txt","r") # HERE "r" used for read and "w" for write

# print(family.readable()) #CHECKS IF FILE IS READABLE
#  print(family.read()) 
# print(family.readline()) #reades first line

#  print(family.readlines()) # give output in form of array 

# family.close()  # FILE MUST BE CLOSED

#***************************************Writing in file************************************
appendmember= open("filee.txt","a")

print(appendmember.writable())
appendmember.write("\n Nabeel Hassan - little brother")
appendmember.write("\n Ashar - cousin brother")
# print(appendmember.read())
appendmember.close()
