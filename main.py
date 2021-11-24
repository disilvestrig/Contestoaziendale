import csv
import time

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def newStudent():
    print("\n")
    file = open("people.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    file = open("people.csv", "a")
    name = input("Nome del nuovo studente: ")
    surname = input("Cognome del nuovo studente: ")
    newStudentNumber = len(rows) + 1
    
    file.write("\n" + name + "," + surname + "," + str(newStudentNumber))
    print("Studente registrato con successo!\n")
    file.close()
def get_people():
	people = []
	while True:
		try:
			n = int(input("Quante persone(1-10)? "))

			while n <= 0 or n > 10:
				print("Devi inserire un numero da 1 a 10")
				n = int(input("Quante persone(1-10)? "))
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

			while n <= 0 or n > 10:
				print("Devi inserire un numero da 1 a 10")
				n = int(input("Quante materie(1-10)? "))
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
					"IDMateria": input("IDMateria: "),
					"IDEsame": i+1,
					"Esito": "NON SVOLTO",
					"Orario" : "",
				})
				while (esami[i]["IDStudente"] < minindex or esami[i]["IDStudente"] >maxindex):
					esami[i]["IDStudente"] = input("Non esiste studente con questo ID reinseriscilo >>> ")
				while (esami[i]["IDMateria"] < minindex2 or esami[i]["IDMateria"] > maxindex2):
					
					esami[i]["IDMateria"] = input("Non esiste materia con questo ID reinseriscilo >>> ")
			return esami
		except:
			print("Errore")

def assign_mark():
	file = open("esami.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()
	minindex = 0
	maxindex = len(rows)-1

	while True:
		try:
			for i in range(len(rows)):
				print("\n")
				for j in range(len(rows[0])):
					print(header[j]+" : "+rows[i][j])
					
			n = int(input("Inserisci l'ID dell'esame da registrare : "))
			while n < minindex +1 or n > maxindex +1:
				print("Non esiste un esame con questo ID reinseriscilo ")
				n = input("Inserisci l'ID dell'esame da registrare : ")
			voto = int(input("Inserisci voto dell'esame ( >=18 e <= 30 ) : "))
			while voto < 18 or voto > 30 :
				voto = input("Inserisci voto dell'esame ( >=18 e <= 30 ) : ")
			rows[n-1][3] = voto
			rows[n-1][4] = time.strftime("%d/%B/%Y"+ " "+"%H:%M:%S")
			if (input("\nVuoi modificare un'altro esame (schiaccia 1 per sì) : ") != "1"):
				return rows
		except:
			print("Error!")

command = input("Quale file vuoi sovrascrivere? (1 per studenti , 2 per materie, 3 per esami, 4 per aggiungere uno studente al file studenti, 5 per scrivere l'esito di un esame) >>> ")
while (command != "1" and command != "2" and command != "3" and command != "4" and command != "5"):
	command = input("Input non valido , inserire 1 o 2 o 3 o 4 o 5 >>> ")
if command == "4":
	newStudent()
	exit()


if ( command == "1"):
	list = get_people()
	csv = "Nome,Cognome,Matricola"
	print("Programma chiuso ...")
elif (command == "2"):
	list = make_matfile()

	csv = "Materia,IDMateria"
	print("Programma chiuso ...")
elif (command == "3" ):
	if checkFileExistance("./materie.csv") == False or checkFileExistance("./people.csv") == False:
		print("Mancano i requisiti sufficienti per creare la tabella esami , controlla l'esistenza dei file materie.csv e people.csv")
		exit()
	list = link_subandstu()
	csv = "IDStudente,IDMateria,IDEsame,Esito,Orario"
	print("Programma chiuso ...")
elif (command == "5"):
	if checkFileExistance("./esami.csv") == False :
		print("Mancano i requisiti sufficienti per modificare la tabella esami , controlla l'esistenza del file esami.csv")
		exit()
	list = assign_mark()
	csv = "IDStudente,IDMateria,IDEsame,Esito,Orario"
	print("Programma chiuso ...")
	

for p in list:
	if (command == "1"):
		csv += "\n{},{},{}".format(p["Nome"], p["Cognome"], p["Matricola"])
	elif command == "2":
		csv += "\n{},{}".format(p["Materia"], p["IDMateria"])
	elif command == "3" :
		csv += "\n{},{},{},{},{}".format(p["IDStudente"],p["IDMateria"],p["IDEsame"],p["Esito"],p["Orario"])
	elif command == "5" :
		csv += "\n{},{},{},{},{}".format(p[0],p[1],p[2],p[3],p[4])
if command == "1":
	f = open("people.csv", "w")
	f.write(csv)
elif command == "2" :
	f = open("materie.csv", "w")

	f.write(csv)
elif command == "3" or command == "5" :
	f = open("esami.csv","w")
	f.write(csv)



f.close()
