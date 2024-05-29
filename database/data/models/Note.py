from dataclasses import dataclass


@dataclass
class Note:
    id: int | None
    name: str
    text: str
    person_id: int

    @staticmethod
    def of(data: tuple):
        return Note(data[0], data[1], data[2], data[3])

    def to_data(self):
        return self.name, self.text, self.person_id

    def get(self):
        return (str(self.id), self.name,
                self.text, str(self.person_id))
