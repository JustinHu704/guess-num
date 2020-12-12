import random
i = 0
start = input('Please determine the starting value of the random number.: ')
end = input('Please determine the ending value of the random number.: ')
end = int(end)
start = int(start)
num = random.randint(start, end)
while True:
	guess = input('Please enter your guess.: ')
	guess = int(guess)
	i =+ 1
	if guess == num:
		print('Your guession is correct.')
		if i == 1:
			print('You use', i, 'time.')
		else:
			print('You use', i, 'times.')
		break
	elif guess > num:
		print('Your guess is larger than the answer.')
	elif guess < num:
		print('Your guess is smaller than the answer.')
	if i == 1:
		print('You use', i, 'time.')
	else:
		print('You use', i, 'times.')

