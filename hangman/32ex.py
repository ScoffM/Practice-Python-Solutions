from r_sowpods import get_word

def tries(lives):
	pass
	

def guess(target):
	# Initialize
	lives = 6
	clue = '_'*len(target)
	used = ['']
	
	print('Welcome to Hangman')
	
	while clue != target and lives > 0:
		print('You have {} lives left'.format(lives))
		print(clue)
		promt = 'Guess your letter: '
		guess = raw_input(promt).upper()
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
			lives -= 1

	
	if lives == 0:
		print('You lose, the word was ' + target)
	else:
		print('You win!')
	
	again = raw_input('Play again? y/n >')
	if again == 'y':
		main()
	else:
		print('Thanks for playing rate 5/5 on playstore or appstore')
				
	
def main():
	target = get_word()
	guess(target)
	
if __name__ == '__main__':
	main()
