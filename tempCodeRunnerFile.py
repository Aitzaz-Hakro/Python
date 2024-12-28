
def Task03():
   #Find the smallest number in a list:**********************************************************************
   print("Task 3:\n")
   NumberList=[98,56,34,65,57,909,234,53,31,"true"]
   smallest=0
   for row in range(len(NumberList)):
      for col in range(row):
         if NumberList[row]<NumberList[col]:
            smallest=NumberList[row]
   print(smallest)
