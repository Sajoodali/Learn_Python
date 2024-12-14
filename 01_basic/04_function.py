# creat OTP fonction 


import random

def generate_otp(length=5):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

otp = generate_otp()
print(f"Your OTP is: {otp}")