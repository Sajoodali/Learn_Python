pet_name = str.upper((input("Enter a Pet Name : ")))
pet_age = int(input("Enter a Pet Age : "))
# pet_age = 5


if pet_name == "DOG":
    if pet_age < 2:
        food = "Puppy Food"
    else:
        food = "Meat"
elif pet_name == "CAT":
    if pet_age <= 5:
        food = "junior Cat Food"
    else:
        food = "Senior Cat Food"
else:
    print("Only Dog & Cat Food info Avilable")
    exit()


print(food)