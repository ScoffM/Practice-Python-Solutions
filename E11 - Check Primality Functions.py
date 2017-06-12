
candidate = int(raw_input("Type numnber: "))

def check_prime(num):
	for n in range(2,num):
		if num%n == 0:
			return False
	return True

if check_prime(candidate):
	print ("is prime")
else:
	print("isn't prime")

