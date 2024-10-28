from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name, is_alive=True,
                 family_name='Baratheon', eyes='brown', hairs='dark') -> None:
        '''constructor for Baratheon'''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Childe method to handle character's death."""
        self.is_alive = False
        return

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    '''doc string for class lannister'''
    def __init__(self, first_name, is_alive=True, family_name='Lannister',
                 eyes='blue', hairs='light') -> None:
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Childe method to handle character's death."""
        self.is_alive = False
        return

    def __str__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create Lannister characters in a chain."""
        return cls(first_name, is_alive)


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
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, \
          Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
