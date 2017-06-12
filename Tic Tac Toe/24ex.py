def main():
	grid_size = int(raw_input("Enter size of grid"))
	horizontal = ' ---'
	vertical = '|   '
	for row in range(grid_size):
	#for column in range(grid_size):
		print(horizontal*grid_size)
		print(vertical*(grid_size+1))
	print(horizontal*grid_size)
if __name__ == '__main__':
	main()
	
