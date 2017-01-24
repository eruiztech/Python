#!/use/bin/python3

sentence = input("Enter sentence to create acronym: ")
strL = sentence.split()
acronym = ""

for item in strL:
	if item == "and" or item == "by" or item == "in" or item == "of" or item == "on":
		pass
	else:
		acronym = acronym + item[0].capitalize()

print(acronym)