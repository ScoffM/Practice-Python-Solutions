import random

def get_word():
	with open('sowpods.txt','r') as f:
		sowpods = f.readlines()
	
	word = sowpods[random.randint(0,len(sowpods)-1)]
	return word.strip()
	
if __name__ == '__main__':
	pick_word()
