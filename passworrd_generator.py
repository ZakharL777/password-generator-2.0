import random

passcode = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    lenght = int(input('What will be the lenght of your password: '))

    password = ''

    for i in range(lenght):
        random_01 = random.choice(passcode)
        password += random_01

    print(password)
    with open('password.txt', 'w') as f:
        f.write(password)
