

# Assingmnt 01 using if-else / for loop / while loop.


checking = True
lastMsg = "goodBye!"

while checking:
    user_input = input("enter your number (& type 'exit' to stop program!)")

    if user_input == "exit":
        break

    number = int(user_input)

    if number % 2 == 0:
        print("even")
    else:
        print("odd")

    for i in lastMsg:
        print(i)


# # Sajood Ali (PWM 331471)
