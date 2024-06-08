from S1E9 import Character


class Baratheon(Character):
    #your code here
    def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='brown', hairs='dark') -> None:
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    
    def die(self):
        """Childe method to handle character's death."""
        self.is_alive = False
        return
    
    def __str__(self):
        return self.__doc__

# class Lannister(Character):
# 	'''doc string for class lannister'''
    
# 	# decorator
# 	def create_lannister():
# 		''' doc string for method create_lannister'''
# 		...
    #your code here


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    # Cersei = Lannister("Cersei")
    # print(Cersei.__dict__)
    # print(Cersei.__str__)
    # print(Cersei.is_alive)
    # print("---")
    # Jaine = Lannister.create_lannister("Jaine", True)
    # print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()