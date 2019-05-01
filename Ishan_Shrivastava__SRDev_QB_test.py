import random

def comparison(first,second):
	if first > second:
		print (first, " is greater than ", second)
	elif first == second:
		print (first, " is equals to ", second)
	elif first < second:
		print (first, " is less than ",second)

x = random.sample(range(-100,100),5)
y = random.sample(range(-100,100),5)

for i,j in zip(x,y):
	comparison(i,j)
