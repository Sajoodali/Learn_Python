age = int(input("Enter your age : "))
day = "sunday"


price = 12 if age > 8 else 8
discount = price


if day == "Sunday":
    discount -= 2




print(f"your ticket price is : $",price)
print(f"but today is Sunday $2 Discount! total amount is : $",discount)

