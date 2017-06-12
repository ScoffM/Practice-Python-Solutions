n1 = int(raw_input("number: "))
print(n1)
div = [1,n1]

for i in range(2,n1):
	if n1%i == 0:
		div.append(i)

print("the divisors are")

print(div)
	
print(len(div))


