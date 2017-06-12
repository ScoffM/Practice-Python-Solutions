def all_same(items):
	return all(x == items[0] for x in items)

def checkWinner(board):
	'''
	Gets a 3x3 board as a list of lists, randomly looks for the first 
	winner and annoucnes it.
	'''	
	# Flatten the board
	b1d = board[0] + board[1] + board[2]
	
	winners = {
		1: b1d[0:3],
		2: b1d[3:6],
		3: b1d[6:],
		4: b1d[0::4],
		5: b1d[0::3],
		6: b1d[2::3],
		7: b1d[2:8:2],
		8: b1d[1::3]
		}
		

	for key in winners:
		if all_same(winners[key]):
			winner = winners[key][0]
			break
		else:
			winner = 0	
			
	
	print("Player {} won".format(winner))
	
if __name__ == "__main__":
	checkWinner()
