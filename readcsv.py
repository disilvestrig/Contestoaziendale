import csv
file = open("people.csv")
csvreader = csv.reader(file)
header = next(csvreader)
rowspeople = []
for row in csvreader:
	rowspeople.append(row)
file.close()
print("\n")

def viewFile():
	file = open("people.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()
	print("\n")
	for i in range(len(rows)):
		for j in range(len(rows[0])):
			print(header[j]+" : "+rows[i][j])
		print("\n")

def searchmat():
	file = open("people.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()
	print("\n")
	count = 0
	n = input("Inserisci numero matricola da cercare : ")
	for i in range(len(rows)):
		matr = rows[i][2]
		if matr == n:
			print("Nome : {}\nCognome : {}\nMatricola : {}".format(rows[i][0],rows[i][1],rows[i][2]))
			count += 1
	if count == 0:
		print("0 people found")
	return n

def show_exams(n):
	esami=[]
	exams=[]
	file = open("esami.csv")
	csvreader = csv.reader(file)
	header = next(csvreader)
	rows = []
	for row in csvreader:
		rows.append(row)
	file.close()
	file2 = open("materie.csv")
	csvreader2 = csv.reader(file2)
	header2 = next(csvreader2)
	rows2 = []
	for row in csvreader2:
		rows2.append(row)
	file2.close()
	for i in rows:
		if i[0] == n:
			esami.append([i[1],0])
	for i in (esami):
		for j in (esami):
			if (i[0] == j[0]):
				i[1] += 1
		exams.append(i)
	uniquelist_exams = []
	[uniquelist_exams.append(x) for x in exams if x not in uniquelist_exams]
	print("ESAMI MANCANTI : ")
	for i in uniquelist_exams:
		for j in rows2:
			if i[0] == j[1]:
				print(str(j[0])+" x"+str(i[1]))
viewFile()


command = input("Vuoi eseguire la funzione di ricerca? (1 per sì , 2 per no) >>> ")
while (command != "1" and command != "2"):
	command = input("Input non valido , inserire 1 o 2 >>> ")

if ( command == "1"):
	n = searchmat()
	if int(n) > len(rowspeople):
		print("Programma chiuso ...")
		exit()
	if input("Vuoi sapere che esami deve ancora svolgere lo/la studente/studentessa ? (digita 1 per sì) >>> ") == "1":
		show_exams(n)
	print("Programma chiuso ...")
else:
	print("Programma chiuso ...")
