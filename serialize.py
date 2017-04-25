import json
import datetime


class Person:
    def __init__(self, obj):
        self.__dict__ = obj

    def __str__(self):
        return str(self.__dict__)


with open("persons.json") as f:
    data = json.load(f)

for p in data["persons"]:
    print(Person(p))

dt = datetime.datetime.now()
print(dt.__format__("%Y-%m-%dT00:00:00"))
