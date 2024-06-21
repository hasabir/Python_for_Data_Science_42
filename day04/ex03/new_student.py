import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
	return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
	name: str
	surname: str
	# active: True


def main():
	student = Student(name = "Edward", surname = "agle")
	student2 = Student(name = "Edward", surname = "agle", id = "toto")
	print(student)
	print(student2)


if __name__ == "__main__":
	main()