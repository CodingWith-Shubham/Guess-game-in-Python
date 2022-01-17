import random
randomNo = random.randint(1,5)
print("********WELCOME TO THIS GUESS GAME*************\n It will run only 10 times\n")
for i in range(1,10):
	a = int(input("Enter your guess::: from 1 to 5::::::"))
	if a == randomNo:
		print("The guess is right , you won!!!!")
	else:
		if a>randomNo:
			print("The guess is wrong :( enter a smaller number")
		elif a<randomNo:
			print("The guess is wrong enter a larger number")
			
print("your trial has finished please purchase the game for 1000$ \n contact: 9315599887")
	