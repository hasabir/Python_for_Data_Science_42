import sys as sys


def main():
	try:
		if (len(sys.argv) != 3 or not sys.argv[2].isnumeric()):
			raise(AssertionError('the arguments are bad'))
		else:
			arr = [s for s in sys.argv[1].split() if s.isalnum()]
			print([s for s in arr if (lambda s: len(s) > int(sys.argv[2]))(s)])
	except AssertionError as e:
		print('AssertionError: ',e)

if __name__ == "__main__":
	main()