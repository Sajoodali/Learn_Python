user_input = int(input("enter your age :"))



if user_input < 13:
    print("You are Child.")
elif user_input < 20:
    print("You are Teenager")
elif user_input < 60:
    print("You are Adult.")
else:
    print("You are senior(60+)")
