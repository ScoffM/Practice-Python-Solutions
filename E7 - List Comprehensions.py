from random import randint as rnd

list_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def ranlist(min_size=5, max_size=15):
	list_size = rnd(min_size, max_size)
	ranlist = []
	while len(ranlist) < list_size:
		ranlist.append(rnd(1,100))
	return ranlist

def evenele(a):
	na = [element for element in a if element % 2 == 0]
	return na

def main():
	list_1 = evenele(list_a)
	list_b = ranlist()
	list_2 = evenele(list_b)
	print(list_1)
	print(list_2)

if __name__ == '__main__':
	main()



