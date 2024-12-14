gread = int(input("Enter Your number :"))

if gread >= 101:
    print("Please verify your grade again")
    exit()


if gread > 90 :
    print("A")
elif gread > 80 :
    print("B")
elif gread > 70:
    print("C")
elif gread > 60:
    print("D")
else:
    print("F")


