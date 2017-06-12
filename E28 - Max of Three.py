def altmax(*vars):
	num_list = list(vars)
	larger = num_list[0]
	for num in num_list:
		if num > larger:
			larger = num
	return larger

def main():
	print(altmax(1,2,3,4,5))
	print(altmax(1,2,3))
	print(altmax(2,5,1,2,3,48))
		

if __name__ == '__main__':
	main()
