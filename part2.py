# Part 2 of the Python Review lab.

def encode(x, y):
	while not isPrime(x):
		x+=1
	while not isPrime(y):
		y+=1
	if 1 < y < 250 and 500 < x < 1000:
			return x*y
	else:
		print ("invalid input: outside range")


def decode(coded_message):
	pass

def isPrime(num):
	for i in range(2,num):
		if (num % i) == 0:
			return False
	return True