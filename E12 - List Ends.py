from random import randint as rnd

def ranlist(min_size=5, max_size=15):
	list_size = rnd(min_size, max_size)
	o_list = [rnd(0,75) for elem in range(list_size)]
	return o_list

def first_last(i_list):
	return [i_list[0], i_list[-1]]

def main():
	new_list = first_last(ranlist())
	print(new_list)

if __name__ == '__main__':
	main()


