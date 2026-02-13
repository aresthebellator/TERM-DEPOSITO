import os
import json
import csv

def UtenteRoot():
    if not os.path.exists("root.json"):
        utente = input("Scrivi il nuovo nome utente amministratore: ")
        password = input("Scrivi la password: ")
        lista_amministratore = (utente,password)
        with open("root.json",'w') as f:
            json.dump(lista_amministratore,f)
        print("Account amministratore creato!")
    else:
        with open("root.json","r")as f:
            lista_root = tuple(json.load(f))
        return lista_root
    
    
    
    
def AggiungiProdotto():
    prodotto = input("Scrivi il nome del prodotto da aggiungere: ")
    quantità = int(input("Scrivi la quantità del prodotto: "))
    prodotti = {}
    if os.path.exists("Lista.csv"):
        with open("Lista.csv",'r')as file:
            reader = csv.reader(file)
            for riga in reader:
                if riga:
                    prodotti[riga[0]] = int(riga[1])
    if prodotto in prodotti:
        prodotti[prodotto] += quantità
    else:
        prodotti[prodotto] = quantità

    with open("Lista.csv",'w',newline="")as file:
        writer = csv.writer(file)
        for nome,qta in prodotti.items():
            writer.writerow([nome,qta])
    print(f"{quantità} unità di {prodotto} aggiunte")


def RimuoviProdotto():
    visualizza = input("Vuoi visualizzare prima il deposito? (s/n)")
    if visualizza.lower in ["si","s"]:
        with open("Lista.csv",'r')as file:
            contenuto = file.read()
            print(contenuto)
    prodotto = input("Scrivi il nome del prodotto da rimuovere: ")
    quantità = int(input("Scrivi la quantità da rimuovere: "))
    
    prodotti = {}
    if os.path.exists("Lista.csv"):
        with open("Lista.csv",'r')as file:
            reader = csv.reader(file)
            for riga in reader:
                if riga:
                    prodotti[riga[0]] = int(riga[1])
    if prodotto in prodotti:
        if prodotti[prodotto] > quantità:
            prodotti[prodotto] -= quantità
            print(f"Rimosse {quantità} unità di {prodotto} ")
        elif prodotti[prodotto] == quantità:
            del prodotti[prodotto]
            print(f"{prodotto} eliminato completamente")
        else:
            print("Errore: quantità da rimuovere superiore a quella a disponibile.")
    else:
        print("Prodotto non trovato")

    with open("Lista.csv",'w',newline="")as file:
        writer = csv.writer(file)
        for nome,qta in prodotti.items():
            writer.writerow([nome,qta])

def VisualizzaDeposito():
    with open("Lista.csv",'r') as file:
        contenuto = file.read()
        print(contenuto)
    
    print("\n")
    scelta = input("Vuoi aggiornare qualcosa nel deposito? (s/n)")
    if scelta.lower() in ["s","si"]:
        print("[1] Aggiungere prodotto")
        print("[2] Rimuovere o modificare prodotto")
        scelta = input("==> ")
        if scelta == 1:
            AggiungiProdotto()
        elif scelta == 2:
            RimuoviProdotto()
        else:
            print("Hai selezionato un opzione non valida")
    else:
        return 0


def PrivilegiAmministratore():
    print("[1] Aggiungere un prodotto")
    print("[2] Rimuovere un prodotto")
    print("[3] Visualizza deposito")
    scelta = input("Scegli cosa fare: ")

    if scelta == 1:
        AggiungiProdotto()
    elif scelta == 2:
        RimuoviProdotto()
    elif scelta == 3:
        VisualizzaDeposito()

def Main():
    lista_root = UtenteRoot()
    a = input("Sei amministratore? (s/n): ")
    if a.lower() in ["si","s"]:
        utente = input("Utente: ")
        password = input("Password: ")
    
    while True:
            if (utente,password) == lista_root:
                print("Accesso amministratore riuscito! ")
                PrivilegiAmministratore()
            else:
                print("Accesso negato")
            
            continua = input("Vuoi riavviare il programma? (s/n): ")
            if continua.lower() in ["no","n"]:
                break


if __name__ == "__main__":
    Main()
    