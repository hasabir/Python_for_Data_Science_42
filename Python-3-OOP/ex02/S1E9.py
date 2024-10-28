from abc import ABC, abstractmethod


class Character(ABC):
    """Base class for a character."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True) -> None:
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to handle character's death."""
        pass


class Stark(Character):
    """Stark: Child class for a character"""
    def __init__(self, first_name, is_alive=True) -> None:
        """Constructor for Stark"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Childe method to handle character's death."""
        self.is_alive = False
        return


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
