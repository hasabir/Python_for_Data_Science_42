import sys as sys

def whatIs():
	try:
		if len(sys.argv) != 2:
			raise AssertionError('more than one argument is provided')
		if not (sys.argv[1]).isdigit():
			raise AssertionError('argument is not an integer')
		if int(sys.argv[1]) % 2 == 0 :
			print('I\'m Even')
			return
		print('I\'m Odd')
	except AssertionError as e:
		print('AssertionError:',e)

whatIs()