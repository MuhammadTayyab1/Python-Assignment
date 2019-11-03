import datetime

x = datetime.datetime.now()

x=str(x)
arr=x.split(" ")

print("Date : ",arr[0])
print("Time : ",arr[1])