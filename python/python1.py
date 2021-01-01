a=int(input("enter the value of the draw:"))
z500=z200=z100=z50=z20=z10=z5=z1=0
if a>=500:
    z500=a//500
    w=int(z500)*500
    a=a-w

if a>=200:
    z200=a//200
    w=int(z200)*200
    a=a-w

if a>=100:
    z100=a//100
    w=int(z100)*100
    a=a-w

if a>=50:
    z50=a//50
    w=int(z50)*50
    a=a-w

if a>=20:
    z20=a//20
    w=int(z20)*20
    a=a-w

if a>=10:
    z10=a//10
    w=int(z10)*10
    a=a-w

if a>=5:
    z5=a//5
    w=int(z5)*5
    a=a-w
if a>=1:
    z1=a//1
    w=int(z1)*1
    a=a-w
print(f"{z1} 1SR\n{z5} 5SR\n{z10} 10SR\n{z20} 20SR\n{z50} 50SR\n{z100} 100SR\n{z200} 200SR\n{z500} 500SR\n")

