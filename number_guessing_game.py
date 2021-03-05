import random
import math

small = int(input("Enter smallest number: "))
big = int(input("Enter big number: "))

num = random.randint(small, big)
print("\n\tYou've only ", round(math.log(big - small + 1, 2)), " chances to guess the integer!\n)")

attempts = 0

while attempts < math.log(big - small + 1, 2):
    attempts += 1

    guess = int(input("Guess a number: "))

    if num == guess:
        print("Congratulations you did it in ", attempts, " try")
        break
    elif num > guess:
        print("You guessed too small")
    elif num < guess:
        print("You guessed too high")

if attempts >= math.log(big - small + 1, 2):
    print("\nThe number is %d" % num)
    print("\tBetter Luck Next time")