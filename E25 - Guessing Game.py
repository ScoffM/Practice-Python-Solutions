def main():
	performance = guess(1)
	end_game(performance)
	
	
def guess(tries):
	lower_limit = 0
	upper_limit = 101

	while True:
		space = range(lower_limit, upper_limit)
		get_guess = space[len(space)/2]
		print("Is it {}?".format(get_guess))
		won = raw_input("'h', 'l' or 'r' >")
		if won == 'y':
			return tries
		elif won == 'l':
			upper_limit = get_guess
			tries += 1
		elif won == 'h':
			lower_limit = get_guess
			tries += 1
		else:
			'Please use proper input'
		
		
def end_game(tries):
	print("I won, took me {} tries".format(tries))
	
if __name__ == "__main__":
	main()
