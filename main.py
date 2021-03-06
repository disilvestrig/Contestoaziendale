import csv
import time
import os
count = 0
markrows = []
peoplerows = []
subrows = []
header = ['IDStudente', 'IDMateria', 'IDEsame', 'Esito', 'Orario']

def readcsv(nomefile):
    file = open(nomefile)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

if (checkFileExistance("people.csv") == True):
    peoplerows = readcsv("people.csv")

if (checkFileExistance("materie.csv") == True):
    subrows = readcsv("materie.csv")

if (checkFileExistance("esami.csv") == True):
    markrows = readcsv("esami.csv")


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

                fileindex = open("fileindex.txt","w")
                fileindex.write(str(len(people)))
                fileindex.close()
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
                fileindex = open("fileindexmaterie.txt","w")
                fileindex.write(str(len(materie)))
                fileindex.close()
                return materie
        except:
            print("Errore!")
            
def link_subandstu():
    import csv
    print("\n")
    
    minindex = 1
    maxindex = len(peoplerows)

    esami = []

    minindex2 = 1
    maxindex2 = len(subrows)

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
            "Orario" : " ",
        })
        while (int(esami[i]["IDStudente"]) < minindex or int(esami[i]["IDStudente"]) >maxindex):
            esami[i]["IDStudente"] = input("Non esiste studente con questo ID reinseriscilo >>> ")
        while (int(esami[i]["IDMateria"]) < minindex2 or int(esami[i]["IDMateria"]) > maxindex2):
            
            esami[i]["IDMateria"] = input("Non esiste materia con questo ID reinseriscilo >>> ")
    fileindex = open("fileindexesami.txt","w")
    fileindex.write(str(len(esami)))
    fileindex.close()
    return esami

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
    for i in markrows:

        try:
            if int(i["IDStudente"]) == n:
                esami.append([i["IDMateria"],0])
        except:
            if (int(i[0]) == n):
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
        for j in subrows:
            try:
                if int(i[0]) == j["IDMateria"]:
                    print(str(j["Materia"]+" x"+str(i[1])))
            except:
                if i[0] == j[1]:
                    print(str(j[0])+" x"+str(i[1]))


def newStudent():
    fileindex = open("fileindex.txt","r")
    index = fileindex.readlines()
    fileindex.close()
    file = open("people.csv", "a")
    name = input("Nome del nuovo studente: ")
    surname = input("Cognome del nuovo studente: ")
    newStudentNumber = int(index[0])+1
    fileindex = open("fileindex.txt","w")
    fileindex.write(str(int(index[0])+1))
    fileindex.close()
    
    file.write("\n" + name + "," + surname + "," + str(newStudentNumber))
    print("Studente registrato con successo!\n")
    file.close()

    peoplerows.append([name,surname,str(newStudentNumber)])

def newMateria():
    fileindex = open("fileindexmaterie.txt","r")
    index = fileindex.readlines()
    print(index)
    fileindex.close()
    file = open("materie.csv", "a")
    name = input("Nome del nuova materia: ")
    newMateriaNumber = int(index[0])+1
    fileindex = open("fileindexmaterie.txt","w")
    fileindex.write(str(int(index[0])+1))
    fileindex.close()
    
    file.write("\n" + name + "," + str(newMateriaNumber))
    print("Materia registrata con successo!\n")
    file.close()

    subrows.append([name,str(newMateriaNumber)])

def newEsame():
    fileindex = open("fileindexesami.txt","r")
    peopleindex = open("fileindex.txt","r")
    matindex = open("fileindexmaterie.txt","r")
    index = fileindex.readlines()
    pind = peopleindex.readlines()
    mind = matindex.readlines()
    print(index)
    fileindex.close()
    file = open("esami.csv", "a")
    name = int(input("IDStudente: "))
    while name <0 or name > int(pind[0]):
        print("Not valid")
        name = int(input("IDStudente"))
    mat = int(input("IDMateria: "))
    while mat <0 or mat > int(mind[0]):
        print("Not valid")
        mat = int(input("IDMateria"))    
    newExamNumber = int(index[0])+1
    fileindex = open("fileindexesami.txt","w")
    fileindex.write(str(int(index[0])+1))
    fileindex.close()
    
    file.write("\n" + str(name) + "," + str(mat) + "," + str(newExamNumber)+ ", NON SVOLTO , ")
    print("Esame registrata con successo!\n")
    file.close()

    markrows.append([str(name),str(mat),str(newExamNumber),"NON SVOLTO"," "])
    
def make_payfile():

    index = open("fileindexesami.txt","r")
    pagamenti = []
    n = index.readlines()
    n = int(n[0])
    for i in range(n):
        pagamenti.append({
            "IDEsame": i+1,
            "Costo": input("Inserire cifra da pagare per l'esame con ID " + str(i+1) + ": ")})
        print("-------------------------")
    return pagamenti

def assign_mark():
    import csv
    global count
    global header
    
    count += 1
    minindex = 0
    maxindex = len(markrows)-1

    for i in range(len(markrows)):
        print("\n")
        for j in range(len(markrows[0])):
            print(header[j],end = "")
            print(" : ",end = "")
            try:
                print(markrows[i][j])
            except:
                print(markrows[i][header[j]])
    n = int(input("\nInserisci l'ID dell'esame da registrare : "))
    while n < minindex +1 or n > maxindex +1:
        print("Non esiste un esame con questo ID reinseriscilo ")
        n = input("Inserisci l'ID dell'esame da registrare : ")
    voto = int(input("Inserisci voto dell'esame ( >=18 e <= 30 ) : "))
    while voto < 18 or voto > 30 :
        voto = int(input("Inserisci voto dell'esame ( >=18 e <= 30 ) : "))
    try:
        print("CIHaihcoah")
        markrows[n-1]["Esito"] = voto
        markrows[n-1]["Orario"] = time.strftime("%d/%B/%Y"+ " "+"%H:%M:%S")
    except:
        markrows[n-1][3] = voto
        markrows[n-1][4] = time.strftime("%d/%B/%Y"+ " "+"%H:%M:%S")
    return markrows




while True:
    print("\u001b[92mMen?? principale: \n0 - Esci\n1 - Sovrascrivi file studenti \n2 - Sovrascrivi file materie \n3 - Sovrascrivi file esami \n4 - Visualizza elenco studenti\n5 - Visualizza dati studente\n6 - Visualizza esami da sostenere dallo studente\n7 - Aggiungi un nuovo studente al file studenti gi?? esistente\n8 - Inserisci il costo di ogni esame\n9 - Scrivi l'esito di un esame\n10 - Aggiungi materia\n11 - Aggiungi esame\n")
        
    command = input("\nInserisci il numero dell'opzione che si desidera effettuare: ")
    while (command != "1" and command != "2" and command != "3" and command != "4" and command != "5" and command != "6" and command != "7" and command != "8" and command != "9" and command != "0" and command != "10" and command != "11"):
        command = input("Input non valido, inserire un numero da 0 a 11: ")
    os.system("clear")

    if ( command == "1"):
        if checkFileExistance("./people.csv") == True:
            print("Non puoi riscrivere da 0 il file, causerebbe errori")
            print("Funzione bloccata ...\n")
            continue
        list = get_people()
        csv = "Nome,Cognome,Matricola"
        peoplerows = list
        print("\nOperazione eseguita!\n")
    
    elif (command == "2"):
        if checkFileExistance("./materie.csv") == True:
            print("Non puoi riscrivere da 0 il file, causerebbe errori")
            print("Funzione bloccata ...\n")
            continue
        list = make_matfile()
        subrows = list
        csv = "Materia,IDMateria"
        print("\nOperazione eseguita!\n")
    
    elif (command == "3" ):
        list = link_subandstu()
        markrows = list
        csv = "IDStudente,IDMateria,IDEsame,Esito,Orario"
        print("\nOperazione eseguita!\n")
    
    elif (command == "4"):
        if checkFileExistance("./people.csv") == False :
            print("Mancano i requisiti sufficienti per visualizzare la tabella studenti, controlla l'esistenza del file people.csv")
            print("\nProgramma chiuso ...")
            continue
        viewFile()
        list = []
        print("\nOperazione eseguita!\n")

    elif (command == "5"):
        matricola = searchmat()
        list = []
        print("\nOperazione eseguita!\n")
        
    elif ( command == "6"):
        x = int(input("Inserisci il numero di matricola dello studente in questione: "))
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
    elif command == "10":
        if checkFileExistance("./materie.csv") == False :
            print("Mancano i requisiti sufficienti per modificare la tabella materie, controlla l'esistenza del file materie.csv")
            print("\nProgramma chiuso ...")
            continue
        
        newMateria()
        list = []
        print("\nOperazione eseguita!\n")
    elif command == "11":
        if checkFileExistance("./esami.csv") == False :
            print("Mancano i requisiti sufficienti per modificare la tabella esami, controlla l'esistenza del file esami.csv")
            print("\nProgramma chiuso ...")
            continue
        
        newEsame()
        list = []
        print("\nOperazione eseguita!\n")    
        
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
            try:
                csv += "\n{},{},{},{},{}".format(p[0],p[1],p[2],p[3],p[4])
            except:
                csv += "\n{},{},{},{},{}".format(p["IDStudente"],p["IDMateria"],p["IDEsame"],p["Esito"],p["Orario"])
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
