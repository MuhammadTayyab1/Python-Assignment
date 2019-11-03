u1=input("Enter first name : ")
u2=input("Enter last name : ")

# Word reverse
print(u2," ",u1)

# Character reverse
u= u1+" "+u2
for i in reversed(range(len(u))):
    print(u[i], end="")