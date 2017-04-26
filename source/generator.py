from faker import Factory
from person import Person


def generate():
    fake = Factory.create()
    personList = []
    for i in range(10000):
        name = fake.name()
        address = fake.address()
        email = fake.email()

        person = Person(name, address, email)
        personList.append(person)

    return personList
