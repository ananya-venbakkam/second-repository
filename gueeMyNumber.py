import random

#asks user to guess rnadom number between 1 and 30 in 3 guesses

num = random.randInt(0, 30)

i = 0

while(i < 3):
	guess = input("Enter your number : ")
	if(guess is num):
		print("You guess it right. Yayy!")
		break
	else:
		print("Wrong guess!")
		if(i is 2):
			("Ooops you're out of turns, goodbye!")
