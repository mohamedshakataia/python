x=int(input('enter the number :'))
y=int(input('enter the number1 :'))
c = []
def fun(n):
    for d in str(n):
        if d == '0' or n % int(d) > 0:return False
    return True
for n in range(x, y + 1):
    if fun(n):c.append(n)
print(c)     
        
            