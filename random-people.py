from random import randint

plenaries = ['Plenary A', 'Plenary B', 'Plenary C', 'Plenary D', 'Plenary E', 'Plenary F']
schools = ['School A', 'School B', 'School C']
names = ["John", "Mary", "William", "Anna", "James", "Margaret", "George", "Helen", "Charles", "Elizabeth", "Joseph", "Ruth", "Frank", "Florence", "Robert", "Ethel", "Edward", "Emma", "Henry", "Marie"]

people = [[
	names[randint(0, len(names)-1)],
	schools[randint(0, len(schools)-1)],
	plenaries[randint(0, len(plenaries)-1)],
	plenaries[randint(0, len(plenaries)-1)],
	plenaries[randint(0, len(plenaries)-1)],
	plenaries[randint(0, len(plenaries)-1)]
	] for _ in range(1000)]

everyone = filter(lambda x: len(x) == len(set(x)), people)
print "\n".join(map(lambda l: ",".join(l), everyone))
print len(everyone)