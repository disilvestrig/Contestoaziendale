

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
						"Matricola": input("Matricola: ")
					})
				return people
		except:
			print("Errore!")

people = get_people()

csv = " Nome, Cognome, Matricola:"

for p in people:
	csv += "\n, {}, {}, {}".format(p["Nome"], p["Cognome"], p["Matricola"])

f = open("people.csv", "w")
f.write(csv)
f.close()
