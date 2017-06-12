
while True:
	p1 = raw_input("Type r for rock, p for paper and s for scissors: ")
	if p1 == 'r' or 'p' or 's':
		print("Player 2 turn")
	else:
		break
	p2 = raw_input("Player 2, type r for rock, p for paper and s for scissors: ")
	if p2 == 'r' or 'p' or 's':
		print("The winner is...")
	else:
		break

	if p1 == p2:
		print("Nobody!")
	elif p1 == 'r' and p2 =='s':
		print("P1!!")
	elif p1 == 's' and p2 =='p':
		print("P1!!")
	elif p1 == 'p' and p2 =='r':
		print("P1!!")
	else:
		print("P2!!")

	yes = raw_input("Do you want to play again? y/n")
	if yes == 'n':
		break






