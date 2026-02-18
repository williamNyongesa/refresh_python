import random
random_number = random.randint(1,10)

random_guess = int(input("put in your guess: "))
if random_guess == random_number:
    print(f"you are correct")
elif random_guess < random_number:
    print(f"{random_guess} is lower")
elif random_guess > random_number:
    print(f"{random_guess} is higher")
else:
    print(f"{random_guess} is not a valid number")