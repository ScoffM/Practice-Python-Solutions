a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 13]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

c = [elem for elem in set(a) if elem in b ]
print(a)
print(b)
print(c)


