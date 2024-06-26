def all_thing_is_obj(object: any) -> int:
    if (isinstance(object, int)):
        print('Type not found')
    elif (isinstance(object, str)):
        print(object, 'is in the kitchen :', type(object))
    else:
        print(type(object).__name__.capitalize(), ':', type(object))
    return 42
