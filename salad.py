
salad_db = open("salads.txt")
my_list = []

for line in salad_db:
	entry = line.strip('^M')
	ing_name = entry.split(",")
	print ing_name


