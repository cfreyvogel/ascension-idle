from oracle import ORACLE
from random import shuffle
from lib.person import Person
from lib.utils import GET_TRUNC_NORM, GLOBALS
with open("resources/first_names.txt","r") as names:
    first_names = [x.strip() for x in names.readlines()]
    shuffle(first_names)

with open("resources/last_names.txt","r") as names:
    last_names = [x.strip() for x in names.readlines()]
    shuffle(last_names)

people = []
for i in range(10):
    people.append(Person(GET_TRUNC_NORM(40,1,GLOBALS["MAX_AGE"],25), (first_names.pop(), last_names.pop())))
for p in people:
    print(p)