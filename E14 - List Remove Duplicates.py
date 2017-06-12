def main():
	taken_list = input()
	set_list = unique_elem_set(taken_list)
	lista_list = unique_elem_list(taken_list)
	print(set_list)
	print(lista_list)

def unique_elem_set(raw_list):
	unique_list = list(set(raw_list))
	return unique_list

def unique_elem_list(raw_list):
	unique_list = []
	for elem in raw_list:
		if elem not in unique_list:
	
			unique_list.append(elem)
	return unique_list

if __name__ == '__main__':
	main()


