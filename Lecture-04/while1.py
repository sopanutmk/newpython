import random

print("What is my magic number (1 to 100)?")
mynumber = random.randint(1, 100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess not mynumber:
    msg = str(ntries) + ">>"
    if (ntries == 6):
        
        
    yourguess = int (input(msg))
    if :
        print("--> too high")
        
    
        print("--> too low")
    ntries += 1
    
if :
    print("Yes! it's " mynumber)
else:
    print("sorry! my number is", mynumber)