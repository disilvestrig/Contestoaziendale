import csv
import time

count = 0
file = open("esami.csv","w")
csvreader = csv.reader(file)
examsrows = []
header = next(csvreader)
for row in csvreader:
    examsrows.append(row)
file.close()
def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False
    
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
    import csv
    print("\n")
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

def viewFile():
    import csv
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
    import csv
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
    import csv
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

def newStudent():
    import csv
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
    
def make_payfile():
    import csv
    file = open("esami.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    
    pagamenti = []
    n = len(rows)
    for i in range(n):
        pagamenti.append({
            "IDEsame": rows[i][2],
            "Costo": input("Inserire cifra da pagare per l'esame con ID " + rows[i][2] + ": ")})
        print("-------------------------")
    return pagamenti

def assign_mark():
    import csv
    minindex = 0
    maxindex = len(examsrows)-1
    global count

    while True:
        try:
            if count == 0:
                for i in range(len(examsrows)):
                    print("\n")
                    for j in range(len(examsrows[0])):
                        print(header[j]+" : "+examsrows[i][j])
            count += 1

            n = int(input("\nInserisci l'ID dell'esame da registrare : "))
            while n < minindex +1 or n > maxindex +1:
                print("Non esiste un esame con questo ID reinseriscilo ")
                n = input("Inserisci l'ID dell'esame da registrare : ")
            voto = int(input("Inserisci voto dell'esame ( >=18 e <= 30 ) : "))
            while voto < 18 or voto > 30 :
                voto = input("Inserisci voto dell'esame ( >=18 e <= 30 ) : ")
            examsrows[n-1][3] = voto
            examsrows[n-1][4] = time.strftime("%d/%B/%Y"+ " "+"%H:%M:%S")
            return examsrows
        except:
            print("Error!")



while True:
    print("Menù principale: \n1 - Sovrascrivi file studenti \n2 - Sovrascrivi file materie \n3 - Sovrascrivi file esami \n4 - Visualizza elenco studenti\n5 - Visualizza dati studente\n6 - Visualizza esami da sostenere dallo studente\n7 - Aggiungi un nuovo studente al file studenti già esistente\n8 - Inserisci il costo di ogni esame\n9 - Scrivi l'esito di un esame\n0 - Esci\n ")
        
    command = input("\nInserisci il numero dell'opzione che si desidera effettuare: ")
    while (command != "1" and command != "2" and command != "3" and command != "4" and command != "5" and command != "6" and command != "7" and command != "8" and command != "9" and command != "0"):
        command = input("Input non valido, inserire un numero da 0 a 9: ")


    if ( command == "1"):
        list = get_people()
        csv = "Nome,Cognome,Matricola"
        print("\nOperazione eseguita!\n")
    
    elif (command == "2"):
        list = make_matfile()
        csv = "Materia,IDMateria"
        print("\nOperazione eseguita!\n")
    
    elif (command == "3" ):
        if checkFileExistance("./materie.csv") == False or checkFileExistance("./people.csv") == False:
            print("Mancano i requisiti sufficienti per creare la tabella esami , controlla l'esistenza dei file materie.csv e people.csv")
            print("\nProgramma chiuso ...")
            exit()
        list = link_subandstu()
        csv = "IDStudente,IDMateria,IDEsame,Esito,Orario"
        print("\nOperazione eseguita!\n")
    
    elif (command == "4"):
        viewFile()
        list = []
        print("\nOperazione eseguita!\n")

    elif (command == "5"):
        matricola = searchmat()
        list = []
        print("\nOperazione eseguita!\n")
        
    elif ( command == "6"):
        x = input("Inserisci il numero di matricola dello studente in questione: ")
        show_exams(x)
        list = []
        print("\nOperazione eseguita!\n")
    
    elif ( command == "7"):
        if checkFileExistance("./people.csv") == False :
            print("Mancano i requisiti sufficienti per modificare la tabella studenti, controlla l'esistenza del file people.csv")
            print("\nProgramma chiuso ...")
            exit()
        
        newStudent()
        list = []
        print("\nOperazione eseguita!\n")
        
    elif ( command == "8"):
        list = make_payfile()
        csv = "IDEsame,Costo"
        print("\nOperazione eseguita!\n")
    
    elif ( command == "9"):
        if checkFileExistance("./esami.csv") == False:
            print("Mancano i requisiti sufficienti per modificare la tabella esami, controlla l'esistenza del file esami.csv")
            print("\nProgramma chiuso ...")
            exit()
        list = assign_mark()
        csv = "IDStudente,IDMateria,IDEsame,Esito,Orario"
        print("\nOperazione eseguita!\n")
        
    elif (command == "0"):
        print("\nProgramma chiuso ...")
        exit()
        
        
    for p in list:
        if (command == "1"):
            csv += "\n{},{},{}".format(p["Nome"], p["Cognome"], p["Matricola"])
        elif command == "2":
            csv += "\n{},{}".format(p["Materia"], p["IDMateria"])
        elif command == "3" :
            csv += "\n{},{},{},{},{}".format(p["IDStudente"],p["IDMateria"],p["IDEsame"],p["Esito"],p["Orario"])
        elif command == "8":
            csv += "\n{},{}".format(p["IDEsame"], p["Costo"]+" euro")
        elif command == "9" :
            csv += "\n{},{},{},{},{}".format(p[0],p[1],p[2],p[3],p[4])
    if command == "1":
        f = open("people.csv", "w")
        f.write(csv)
    elif command == "2" :
        f = open("materie.csv", "w")
        f.write(csv)
    elif command == "3" or command == "9" :
        f = open("esami.csv","w")
        f.write(csv)
    elif command == "8":
        f = open("pagamenti.csv", "w")
        f.write(csv)

f.close()
