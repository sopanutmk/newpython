inchar = input("input one character : ")
if inchar >= "A" and inchar <= "Z":
    print("You input Upper case Letter",inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You input Lower case Letter",inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input Number",inchar)
else:
    print("It's not a letter of number",inchar)
    