import os
import json
import csv


def UtenteRoot():
    if not os.path.exists("root.json"):  # prima volta
        utente = input("Scrivi il nome utente root:\n")
        password = input("Scrivi la password root:\n")
        lista_root = (utente, password)
        with open("root.json", "w") as f:
            json.dump(lista_root, f)
        print("Account root creato ✅")
    else:
        with open("root.json", "r") as f:
            lista_root = tuple(json.load(f))
    return lista_root

def PrivilegiUtente():
    scelta = input("Scegli cosa fare:\n(1) Aggiungere un prodotto\n(2) Rimuovere un prodotto\n(3) Visualizza deposito\n> ")

    if scelta == "1":
        prodotto = input("Scrivi il nome del prodotto da aggiungere:\n> ")
        quantita = int(input("Scrivi la quantità da aggiungere:\n> "))

        # Carica prodotti esistenti
        prodotti = {}
        if os.path.exists("Lista.csv"):
            with open("Lista.csv", "r") as file:
                reader = csv.reader(file)
                for riga in reader:
                    if riga:
                        prodotti[riga[0]] = int(riga[1])

        # Aggiunge o aggiorna la quantità
        if prodotto in prodotti:
            prodotti[prodotto] += quantita
        else:
            prodotti[prodotto] = quantita

        # Riscrive il file aggiornato
        with open("Lista.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for nome, qta in prodotti.items():
                writer.writerow([nome, qta])

        print(f"{quantita} unità di {prodotto} aggiunte ✅")

    elif scelta == "2":
        
        visualizza = input("Vuoi visualizzare prima il deposito? (s/n)")
        if visualizza.lower() in ["si","s"]:
            with open("Lista.csv",'r') as file:
                contenuto = file.read()
                print(contenuto)

        
        prodotto = input("Scrivi il nome del prodotto da rimuovere:\n> ")
        quantita = int(input("Scrivi la quantità da rimuovere:\n> "))

        # Carica prodotti
        prodotti = {}
        if os.path.exists("Lista.csv"):
            with open("Lista.csv", "r") as file:
                reader = csv.reader(file)
                for riga in reader:
                    if riga:
                        prodotti[riga[0]] = int(riga[1])

        # Rimuove quantità
        if prodotto in prodotti:
            if prodotti[prodotto] > quantita:
                prodotti[prodotto] -= quantita
                print(f"Rimosse {quantita} unità di {prodotto} ")
            elif prodotti[prodotto] == quantita:
                del prodotti[prodotto]
                print(f"{prodotto} eliminato completamente ")
            else:
                print("Errore: quantità da rimuovere superiore a quella disponibile ")
        else:
            print("Prodotto non trovato ")

        # Riscrive il file aggiornato
        with open("Lista.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for nome, qta in prodotti.items():
                writer.writerow([nome, qta])
    
    
    elif scelta == "3":
        with open("Lista.csv", 'r') as file:
            contenuto = file.read()
            print(contenuto)

# === MAIN PROGRAM ===
def Main():
    
    lista_root = UtenteRoot()  # carica o crea root

    a = input("Sei root? (si/no):\n>")
    if a.lower() in ["si","s"]:
        utente = input("Utente: ")
        password = input("Password: ")
    while True:
            if (utente, password) == lista_root:
                print("Accesso root riuscito ✅")
                PrivilegiUtente()
            else:
                print("Accesso negato ❌")
        
        
            continua = input("Vuoi riavviare il programma? (s/n)\n> ")
            if continua.lower() in ["no","n"]:
                break

         


# Avvio programma
if __name__ == "__main__":
    Main()
