
def comparison(first,second):
	if first > second:
		print (first, " is greater than ", second)
	elif first == second:
		print (first, " is equals to ", second)
	elif first < second:
		print (first, " is less than ",second)

first_value_ = input("Enter the first value: ")
first_value_ = first_value_.replace('"','')
first_value = float(first_value_)

#print ("First Value is: ", first_value_)

second_value_ = input("Enter the second value: ")
second_value_ = second_value_.replace('"','')
second_value = float(second_value_)

#print ("second Value is: ", second_value_)

comparison (first_value, second_value)
