def get_word():
	word = 'EVAPORATE'
	return word
	
def guess(target):
	# Welcome Message
	print(type(target))
	print('Welcome to Hangman')
	clue = '_'*len(target)
	used = list()
	
	while clue != target:
		print(clue)
		promt = 'Guess your letter: '
		guess = raw_input(promt)
		if guess in used:
			print("You already guessed that, silly")
			continue
		if guess in target:
			for i, letter in enumerate(target):
				if letter == guess:
					clue = clue[:i] + guess + clue[i+1:]
			used.append(guess)		
		else:
			print('Incorrect!')


			
	
def main():
	target = get_word()
	guess(target)
	
if __name__ == '__main__':
	main()
