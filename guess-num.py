import random
r = random.randint(1, 100)
while True:
	num = input('Please guess the number: ')
	num = int(num)
	if num == r:
		print('Your guess is correct.')
		break
	elif r > num:
		print('Your guess is smaller than the answer.')
	elif r < num:
		print('Your guess is larger than the answer.')
