x,y,z=input("EXpression: ").split(" ")
x,z=float(x),float(z)
if y=="+":
    print(x+z)
elif y=="-":
    print(x-z)
elif y=="*":
    print(x*z)
else:
    print(x/z)