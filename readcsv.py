import csv
file = open("people.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
print("\n")

def viewFile():
	for i in range(len(rows)):
		for j in range(len(rows[0])):
		    print(header[j]+" : "+rows[i][j])
		print("\n")

def searchmat():
    n = input("Inserisci numero matricola da cercare : ")
    for i in range(len(rows)):
    	matr = rows[i][2]
    	if matr == n:
    		print("uhsogh")
    		print("Nome : {}\nCognome : {}\nMatricola : {}".format(rows[i][0],rows[i][1],rows[i][2]))
viewFile()
searchmat()
