import csv

def get_people():
	people = []
	while True:
		try:
			n = int(input("Quante persone(1-10)? "))

			if n <= 0 or n > 10:
				print("Devi inserire un numero da 1 a 10")
			else:
				for i in range(n):
					print("-------------------------")
					people.append({
						"Nome": input("Nome: "),
						"Cognome": input("Cognome: "),
						"Matricola": i+1
					})
				return people
		except:
			print("Errore!")
def make_matfile():
	materie = []
	while True:
		try:
			n = int(input("Quante materie(1-10)? "))

			if n <= 0 or n > 10:
				print("Devi inserire un numero da 1 a 10")
			else:
				for i in range(n):
					print("-------------------------")
					materie.append({
						"Materia": input("Nome Materia: "),
						"IDMateria": i+1
					})
				return materie
		except:
			print("Errore!")
def link_subandstu():
	
	file = open("people.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()
	minindex = rows[0][2]
	maxindex = rows[len(rows)-1][2]

	esami = []
	file2 = open("materie.csv")
	csvreader2 = csv.reader(file2)
	header2 = next(csvreader2)
	rows2 = []
	for row in csvreader2:
		rows2.append(row)
	file.close()
	minindex2 = rows2[0][1]
	maxindex2 = rows2[len(rows2)-1][1]
	print(maxindex2)


	while True:
		try:
			n = int(input("Inserisci numero di esami: "))
			while n <= 0 or n > 10:
				print("Devi inserire un numero da 1 a 10")
				n = int(input("Inserisci numero di esami: "))
			
			for i in range(n):
				print("-------------------------")
				esami.append({
					"IDStudente": input("IDStudente: "),
					"IDMateria": input("IDMateria: ")
				})
				while (esami[i]["IDStudente"] < minindex or esami[i]["IDStudente"] >maxindex):
					esami[i]["IDStudente"] = input("Non esiste studente con questo ID reinseriscilo >>> ")
				while (esami[i]["IDMateria"] < minindex2 or esami[i]["IDMateria"] > maxindex2):
					
					esami[i]["IDMateria"] = input("Non esiste materia con questo ID reinseriscilo >>> ")
			return esami
		except:
			print("Errore")



command = input("Quale file vuoi sovrascrivere? (1 per studenti , 2 per materie, 3 per esami) >>> ")
while (command != "1" and command != "2" and command != "3"):
	command = input("Input non valido , inserire 1 o 2 o 3 >>> ")

if ( command == "1"):
	list = get_people()
	csv = "Nome,Cognome,Matricola"
	print("Programma chiuso ...")
elif (command == "2"):
	list = make_matfile()
	csv = "Materia,IDMateria"
	print("Programma chiuso ...")
else:
	list = link_subandstu()
	csv = "IDStudente,IDMateria"
	print("Programma chiuso ...")

for p in list:
	if (command == "1"):
		csv += "\n{},{},{}".format(p["Nome"], p["Cognome"], p["Matricola"])
	elif command == "2":
		csv += "\n{},{}".format(p["Materia"], p["IDMateria"])
	else :
		csv += "\n{},{}".format(p["IDStudente"],p["IDMateria"])
if command == "1":
	f = open("people.csv", "w")
elif command == "2":
	f = open("materie.csv", "w")
else :
	f = open("esami.csv","w")
f.write(csv)

f.close()
