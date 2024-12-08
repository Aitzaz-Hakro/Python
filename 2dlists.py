
listt=[
    [4,5,4],
    [1,4,67],
    [2,5,7]
]

for row in listt:
    for col in row:
        print(col)

#************** TRANSALTION PROGRAM : CONVERT VOWELS INTO OTHER WOERD

def translater(phrase):
    translation=""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            translation+="g"
            
        else:
            translation+=letter
    return translation

print(translater(input("Enter a phrase : ")))  
