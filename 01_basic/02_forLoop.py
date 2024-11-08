# simple loop

user_input = input("Enter a msg and start loop: ")

for i in user_input:
    print(i)


# list ka simple loop

user_ = ["apple", "banana", "orange", "graps"]

for i in user:
    print(i)


# input ly ke list creat krna or loop lgana.

user_input = input("Enter items separated by space: ")

input_list = user_input.split()

print("Input List:", input_list)

for i in input_list:
    print(i)


# input ly ke int me list creat krna or loop lgana.

user_input = input("Enter numbers separated by space: ")

input_list = [int(x) for x in user_input.split()]

print("Input List:", input_list)

for i in input_list:
    print(i)
