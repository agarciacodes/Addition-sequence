Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def seq(n):
	total = 0
	lst = []
	eq = '='
	if n < 0:
		return "please enter a non-negative number"
	elif n == 0:
		return 0
	elif type(n) is float:
		return "Please enter a whole number, no decimals"
	else:
		for i in range(0, n+1):
			lst.append(i)
			total += i
		for x in lst:
			if x < n:
				print(x, end = '+')
			else:
				print(x, end = '')
		print(eq + str(total))

		
>>> print(seq(6))
0+1+2+3+4+5+6=21
None
>>> print(seq(-4))
please enter a non-negative number
>>> print(seq(0))
0
>>> print(seq(5.555))
Please enter a whole number, no decimals
>>> 