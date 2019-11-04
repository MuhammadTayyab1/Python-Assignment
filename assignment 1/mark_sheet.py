
#input from user
try:
    percent = int(input("Enter your Percentage : "))

#Using conditions find grade

    if percent >= 80 and percent <=100:
        print("A Grade")
    elif percent >= 70 and percent < 80:
        print("B Grade")
    elif percent >=60 and percent < 70:
        print("C Grade")
    elif percent >=0 and percent <60:
        print("Fail")
    else:
        print("Wrong input try again")

except:
    print("Enter numeric value")