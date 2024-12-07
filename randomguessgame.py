secret_guess="aitzaz"
guess=""
count=0
outofguess=False
guesslimit=3
print("you have three chaces to spell my name: ")

while guess!=secret_guess and not(outofguess):
    if count<guesslimit:
     guess=input("Spell my Name: ")
     count+=1
    else:
       outofguess=True

if outofguess:
   print("0ut of guesses")
else:
  print("Yow spell write!!") 