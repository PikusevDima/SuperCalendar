from dataclasses import dataclass


@dataclass
class Person:
    id: int | None
    login: str
    password: str

    @staticmethod
    def of(data: tuple):
        return Person(data[0], data[1], data[2])

    def to_data(self):
        return self.login, self.password

    def get(self):
        return (str(self.id), self.login,
                self.password)
