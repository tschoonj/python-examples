from dataclasses import dataclass, fields, asdict
import csv

@dataclass
class Person:
    first_name: str
    family_name: str
    age: int

    def __repr__(self) -> str:
        return f"{self.first_name} {self.family_name}, {self.age}"

varun = Person(first_name="Varun", family_name="Kadapatti", age=15)
sanaya = Person(first_name="Sanaya", family_name="Kadapatti", age=19)
sam = Person(first_name="Sam", family_name="Schoonjans", age=7)

people = [varun, sanaya, sam]

filename = "people.csv"
fieldnames = list(map(lambda field: field.name, fields(Person)))

with open(filename, mode="w") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for person in people:
        writer.writerow(asdict(person))

people_from_file: list[Person] = []

with open(filename, mode="r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        people_from_file.append(
            Person(
                first_name=row["first_name"],
                family_name=row["family_name"],
                age=int(row["age"]),
            )
        )

if len(people) != len(people_from_file):
    raise Exception("length of list does not match")

for person, person_from_file in zip(people, people_from_file):
    if person != person_from_file:
        raise Exception("person from file differs from original")





print(f"{varun=}")