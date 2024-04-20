
my_types = {
	'Nothing': 'NoneType',
	'Cheese': 'float',
	'Zero': 'int',
	'Empty': 'str',
	'Fake': 'bool'
}

def NULL_not_found(object: any) -> int:
	if isinstance(object, float) and object != object:
		pass
	elif (object != None and object != 0 and object != '' and object != False):
		print ('Type not Found')
		return 1
	object_type = type(object).__name__
	key = list(my_types.keys())
	value = list(my_types.values())
	print(f'{key[value.index(object_type)]}: {object} {type(object)}')
	return 0

	