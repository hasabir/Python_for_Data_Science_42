import sys as sys

def whatIs():
	if len(sys.argv) < 2:
		return
	try:
		if len(sys.argv) > 2:
			raise AssertionError('more than one argument is provided')
		
		try:
			stock = int(sys.argv[1])
		except ValueError:
			raise AssertionError('argument is not an integer')

		if stock % 2 == 0 :
			print('I\'m Even')
			return
		print('I\'m Odd')
	except AssertionError as e:
		print('AssertionError:',e)

whatIs()