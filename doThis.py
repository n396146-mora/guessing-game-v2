#imports:
import random
#code:
print("Hello user were going to play a guessing game")
low=int(input("Enter the lowest number you want me to choose from: "))
high=int(input("Enter the highest number you want me to choose from: "))
num=0
print("i've chosen my number from " + str(low) + "-" + str(high))
num=random.randint(low,high)
guess=0
tries=0
while(num!=guess):
	guess=int(input("Enter your guess: "))
	tries=tries+1
	if(guess>num):
		print("Try lower")
	else:
		print("Try higher")
if(num==guess):
	print("You got it!")
	print("it  took you " + str(tries) + " tries to guess the number.")