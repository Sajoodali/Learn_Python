number = 29
Is_prim = True

if number > 1:
    for i in range(2 , number):
        if (number % i) == 0:
            Is_prim = False
            break
        
print(Is_prim)