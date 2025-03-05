#WAP a mini project of number series in which start point , end point , updation , choice for horizontal or vertical print and also taking choice for forward and reverse

a = int(input("Enter starting point: "))
b = int(input("Enter ending point: "))
c = int(input("Enter updation: "))
p = str(input("Enter v for vertical or h for horizontal: "))
f = str(input("Enter f for foward and r for reverse: "))

#print(p)
# print(f)
if(f == 'f' or f == 'F'):
    for x in range(a,b+1,c):
        if(p == 'h' or p == 'H' ):
            print(x , end=" ")
        elif(p == 'v' or p == 'V'):
            print(x)
        else:
            print("Invalid input.")
elif(f == 'r' or f == 'R'):
    for x in range(b,a-1,-(c)):
        if(p == 'h' or p == 'H'):
            print(x , end=" ")
        elif(p == 'v' or p == 'V'):
            print(x)
        else:
            print("Invalid input.")
else:
    print("Enter valid itertions!!!!!")