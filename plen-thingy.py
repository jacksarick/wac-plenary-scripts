# Row format
# NAME, SCHOOL, choice 1, choice 2, ... choice n
from collections import Counter

CHOICES = 4
PLENARIES = 6
with open("File\n> ") as everyone:
	for person in everyone:
		person.split()