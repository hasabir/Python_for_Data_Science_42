from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
	def __init__(self, first_name, is_alive=True, family_name='Baratheon', eyes='brown', hairs='dark') -> None:
		super().__init__(first_name, is_alive, family_name, eyes, hairs)

	def set_eyes(self, color):
		'''eyes setter'''
		self.eyes = color
	def set_hairs(self, hairs):
		'''hairs setter'''
		self.hairs = hairs
	def get_eyes(self):
		'''eyes getter'''
		return self.eyes
	def get_hairs(self):
		'''hairs getter'''
		return self.hairs


def main():
	'''doc string for main function'''
	Joffrey = King("Joffrey")
	print(Joffrey.__dict__)
	Joffrey.set_eyes("blue")
	Joffrey.set_hairs("light")
	print(Joffrey.get_eyes())
	print(Joffrey.get_hairs())
	print(Joffrey.__dict__)


if __name__ == "__main__":
	main()
