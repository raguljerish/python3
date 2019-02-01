N=int(input("type the no less than 1000   "))
c=N
x=0
while N>0:
    i=N%10
    N=N//10
    x=str(x)+str(i)
x=int(x)-int(x[0])
if x==c:
    print("yes")
else:
    print("no")
