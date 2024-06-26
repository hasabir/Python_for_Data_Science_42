import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(init=True)
class Student:
    name: str
    surname: str
    active: bool = field(default=True, init=True)
    login: str = field(init=False)
    id: int = field(default=generate_id(), init=False)

    def __post_init__(self):
        self.login = f"{self.name[0]}{self.surname}"


def main():
    student = Student(name="Edward", surname="agle")
    # student2 = Student(name = "Edward", surname = "agle", id = "toto")
    print(student)
    # print(student2)


if __name__ == "__main__":
    main()
