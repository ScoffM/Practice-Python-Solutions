import ticktack

def get_coordinates(grid, player, max_size = 2, min_size = 0):
	valid = False
	while not valid:

		print('     1  2  3')
		for col, row in enumerate(grid):
			print(col+1, row)
		prompt = 'Player {}, input your coordinates as "x,y"'
		coord = raw_input(prompt.format(player))
		x,y  = coord.split(',')
		x = int(x) - 1
		y = int(y) - 1
		if x <= max_size and x >= min_size:
			if y <= max_size and y >= min_size:
				valid = True
			else:
				print('invalid coordinates, try again')
		else:
			print('invalid coordinates, try again')
	return x, y
	

def turn(grid, player):
	x, y = get_coordinates(grid, player)
	if grid[y][x] == 0:
		grid[y][x] = player
		return grid
	else:
		raise ValueError('Coordinates already occupied')
	
def main():
	grid = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

	player = 2

	full = False

	while not full:
		
		# Alternate between players
		if player == 2:
			player = 1
		else:
			player = 2
		
		successful = False
		while not successful:
			try:
				grid = turn(grid,player)
				successful = True
			except ValueError as e:
				print('Error:' , e)
				
		pg = grid[0]+grid[1]+grid[2]
                full = not 0 in pg

	print('Board full...')
	ticktack.checkWinner(grid)

if __name__ == '__main__':
	main()
