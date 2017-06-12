import random as rnd

def main():
	# Load 1000 common words as a list of words
	with open('generator.txt','r') as f:
		words = list(set(f.read().split()))
	
	num_words = input("How many words should be in your password")

	seed_word = [rnd.randint(0,999) for i in range(num_words)]
	
	raw_pass = [words[elem] for elem in seed_word]
	
	req_str = str(raw_input("Choose password strenght: \nlow:'l', \nmed:'m' \nhigh:'h'\n>"))

	if req_str == 'l' or req_str == 'm' or req_str == 'h':
		print('Your password is:')
	else:
		req_str = 'm'
		print('Something went wrong, your medium strenght password is')

	pw = ''
	for word in raw_pass:
		pw += word

	if req_str == 'l':
		# Defaults n words as password
		print("Your password is: {}".format(pw))
	elif req_str == 'm':
		# Capitalizes the first character, then appends a small number
		pw = pw.capitalize()	
		pw = pw + rnd.randint(0,9)	
		print("Your password is: {}".format(pw))
	else:
		# Capitalizes a random character of the password, then appends a larger number 
		n = rnd.randint(0,len(pw))
		pw = pw[:n] + pw[n].upper() + pw[n+1:]
		pw = pw +str(rnd.randint(0,99))
		print("Your password is: {}".format(pw))


		

if __name__ == '__main__':
	main()




