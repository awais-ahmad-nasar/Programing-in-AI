"""create a function that take a list and
return count of positive and negative number """


def count_p_n(list):
	p = 0
	n = 0
	for i in list:
		if i > 0:
			p += 1
		else:
			n += 1
	return p, n


l = [1, -2, 3, -4, 5]
positive, negative = count_p_n(l)
print("Positive count:", positive)
print("Negative count:", negative)

"""create a function that takes a number and return whether it is prime number or not  """


def is_prime(number):
	if number %2==1:
		print("prime number ")
	else:
		print("not prime number ")
	return number
x=eval(input("please enter number "))
is_prime(x)

"""create a function that takes a key and value, and this function will add that value in previous value."""


def add_d(d, k, v):
	if k in d:
		d[k] += v
	else:
		d[k] = v
my_dict = {'a': 10, 'b': 20}
add_d(my_dict, 'aneeq', 55)
add_d(my_dict, 'qamar', 45)
print(my_dict)
