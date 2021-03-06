import random

"""
pick a number and guess the number the computer selected from 0 to the selected number
"""

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")

"""
example 2 for teaching trials


import random

num = random.randint(1,10)
guess = None

while guess != num:
	guess = input("guess a number between 1 and 10: ")
	guess = int(guess)

	if guess == num:
		print("you win")
		break
	else:
		print("try again")


"""