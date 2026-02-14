## ===============================================
## DEPOSITO
## Copyright (c) 2026 aresthebellator
## Version: 1.0 
## ===============================================

import os
import json
import csv

def Scritta():
    
    print("""\033[1;36m
██████  ███████ ██████   ██████  ███████ ██ ████████  ██████  
██   ██ ██      ██   ██ ██    ██ ██      ██    ██    ██    ██ 
██   ██ █████   ██████  ██    ██ ███████ ██    ██    ██    ██ 
██   ██ ██      ██      ██    ██      ██ ██    ██    ██    ██ 
██████  ███████ ██       ██████  ███████ ██    ██     ██████  
    \033[0m""")

def Pulizia():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def UtenteRoot():
    if not os.path.exists("root.json"):
        utente = input("Scrivi il nuovo nome utente amministratore: ")
        password = input("Scrivi la password: ")
        lista_amministratore = [utente, password]
        with open("root.json", 'w') as f:
            json.dump(lista_amministratore, f)
        print("Account amministratore creato!")
        return tuple(lista_amministratore)
    else:
        with open("root.json", "r") as f:
            return tuple(json.load(f))

def AggiungiProdotto():
    Pulizia()
    Scritta()
    prodotto = input("Scrivi il nome del prodotto da aggiungere: ")
    try:
        quantità = int(input("Scrivi la quantità del prodotto: "))
    except ValueError:
        print("Errore: Inserisci un numero valido.")
        return

    prodotti = {}
    if os.path.exists("Lista.csv"):
        with open("Lista.csv", 'r', newline="") as file:
            reader = csv.reader(file)
            for riga in reader:
                if riga:
                    prodotti[riga[0]] = int(riga[1])
    
    if prodotto in prodotti:
        prodotti[prodotto] += quantità
    else:
        prodotti[prodotto] = quantità

    with open("Lista.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        for nome, qta in prodotti.items():
            writer.writerow([nome, qta])
    print(f"{quantità} unità di {prodotto} aggiunte.")
    input("\nPremi Invio per continuare...")

def RimuoviProdotto():
    Pulizia()
    Scritta()
    if not os.path.exists("Lista.csv"):
        print("Errore: Il deposito è vuoto (file non trovato).")
        input("\nPremi Invio...")
        return

    visualizza = input("Vuoi visualizzare prima il deposito? (s/n): ")
    if visualizza.lower() in ["si", "s"]:
        with open("Lista.csv", 'r') as file:
            print("\n--- STATO DEPOSITO ---")
            print(file.read())
            print("----------------------")

    prodotto = input("Scrivi il nome del prodotto da modificare/rimuovere: ")
    try:
        quantità = int(input("Scrivi la quantità da rimuovere: "))
    except ValueError:
        print("Errore: Inserisci un numero.")
        return
    
    prodotti = {}
    with open("Lista.csv", 'r', newline="") as file:
        reader = csv.reader(file)
        for riga in reader:
            if riga:
                prodotti[riga[0]] = int(riga[1])

    if prodotto in prodotti:
        if prodotti[prodotto] > quantità:
            prodotti[prodotto] -= quantità
            print(f"Rimosse {quantità} unità di {prodotto}.")
        elif prodotti[prodotto] == quantità:
            del prodotti[prodotto]
            print(f"{prodotto} eliminato completamente.")
        else:
            print("Errore: quantità da rimuovere superiore a quella disponibile.")
    else:
        print("Prodotto non trovato.")

    with open("Lista.csv", 'w', newline="") as file:
        writer = csv.writer(file)
        for nome, qta in prodotti.items():
            writer.writerow([nome, qta])
    input("\nPremi Invio per continuare...")

def VisualizzaDeposito():
    Pulizia()
    Scritta()
    if os.path.exists("Lista.csv"):
        print("--- CONTENUTO DEPOSITO ---")
        with open("Lista.csv", 'r') as file:
            contenuto = file.read()
            print(contenuto if contenuto.strip() else "Il deposito è vuoto.")
        print("--------------------------")
    else:
        print("Errore, file Lista.csv non trovato.")
    
    scelta = input("\nVuoi aggiornare qualcosa? (s/n): ")
    if scelta.lower() in ["s", "si"]:
        print("[1] Aggiungere prodotto")
        print("[2] Rimuovere o modificare prodotto")
        sottoscelta = input("==> ")
        if sottoscelta == "1":
            AggiungiProdotto()
        elif sottoscelta == "2":
            RimuoviProdotto()

def PrivilegiAmministratore():
    while True:
        Pulizia()
        Scritta()
        print("--- MENU AMMINISTRATORE ---")
        print("[1] Aggiungere un prodotto")
        print("[2] Rimuovere un prodotto")
        print("[3] Visualizza deposito")
        print("[4] Torna al login / Esci")
        
        scelta = input("Scegli cosa fare: ")

        if scelta == "1":
            AggiungiProdotto()
        elif scelta == "2":
            RimuoviProdotto()
        elif scelta == "3":
            VisualizzaDeposito()
        elif scelta == "4":
            break
        else:
            print("Opzione non valida.")

def Main():
    while True:
        lista_root = UtenteRoot()
        Pulizia()
        Scritta()
        a = input("Sei amministratore? (s/n) [scrivi 'esci' per chiudere]: ")
        
        if a.lower() == "esci":
            break
            
        if a.lower() in ["si", "s"]:
            utente = input("Utente: ")
            password = input("Password: ")
            
            if (utente, password) == lista_root:
                print("Accesso riuscito!")
                PrivilegiAmministratore()
            else:
                print("Accesso negato! Credenziali errate.")
                input("Premi Invio per riprovare...")
        else:
            print("Accesso limitato non implementato. Solo admin.")
            input("Premi Invio...")

if __name__ == "__main__":
    Main()
