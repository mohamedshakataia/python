x=input("enter the character:")
b=ord(x)               #command to convert letters to numbers
if (b>=65 and b<=90  ):
    print(chr(b+32))   # chr:command to convert letters to numbers
else:
    print(chr(b-32))
