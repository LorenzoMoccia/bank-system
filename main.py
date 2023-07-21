from getpass import getpass


# Definisco la classe 'Conto'
class Conto:

    # Costruttore
    def __init__(self, saldo, proprietario, id):
        self.saldo = saldo
        self.proprietario = proprietario
        self.transaction_counter = 0
        self.transactions = []
        self.id = id

    # Metodo deposito
    def deposito(self):
        valore = int(input("Inserisci la cifra da depositare: "))
        self.saldo += valore
        self.transaction_counter = self.transaction_counter + 1
        transaction = f"Transazione #{self.transaction_counter}: Deposito di {valore}€."
        self.transactions.append(transaction)

    # Metodo prelievo
    def prelievo(self):
        valore = int(input("Inserisci la cifra da prelevare: "))

        # Controllo se il saldo è maggiore del prelievo
        if self.saldo >= valore:
            self.saldo -= valore
            self.transaction_counter = self.transaction_counter + 1
            transaction = f"Transazione #{self.transaction_counter}: Prelievo di {valore}€."
            self.transactions.append(transaction)
        else:
            print("Saldo insufficiente!")

    # Metodo stampa
    def stampa_saldo(self):
        print(str(self.saldo) + "€")

    # Metodo stampa informazioni
    def informazioni(self):
        return f'Conto: Proprietario: {self.proprietario}.\nSaldo: {self.saldo}€.'

    # Metodo visualizza storico transazioni
    def visualizza_transazioni(self):
        for transaction in self.transactions:
            print(transaction)



#Definisco la classe Adminin
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auth = False
        self.counter = 0

    #Crea conto
    def add_conto(self):
        if mio_admin.auth == True:
            saldo = input("Inserisci il saldo iniziale del conto: ")
            proprietario = input("Inserisci il nome e cognome del proprietario: ")
            self.counter = self.counter + 1
            conto = Conto(saldo, proprietario, self.counter)
            conti.append(conto)
            print("Conto creato con succcesso!")
        else:
            print("C'è stato un errore nella creazione del conto.")

    #Visualizza lista conti
    def view_conti(self):
        for conto in conti:
            print("_"*50)
            print(f"Conto #{conto.id}")
            print(f"Proprietario: {conto.proprietario}")
            print(f"Saldo: {conto.saldo}")
            print("_"*50)
            
            








# MAIN PROGRAM

#ISTANZE
mio_admin = Admin("admin", "test")
mio_conto = Conto(0, "Lorenzo Moccia", 0)


#Array di oggetti Conto
conti = []



#METHODS
def admin_login():
    username = input("Inserisci username dell'admin:\n")
    password = getpass("Inserisci password:\n")

    #Controllo username e password che corrispondano
    if (username == "admin" and mio_admin.username == "admin") and (password == mio_admin.password and mio_admin.password == "test"):
        print(f"Bentornato {mio_admin.username}, ora puoi usare le funzionalità di admin.!")
        mio_admin.auth = True
    else:
        print("Username o password errati!")


# Imposto una variabile a True per fare un loop infinito del programma.
continua = True


#MENU
print("Benvenuto nel Bank-Account software!")
print("[1] Deposito.\n[2] Prelievo.\n[3] Informazioni.\n[4] Saldo.\n[5] Visualizza storico transazioni.\n[6] Admin Control Panel\n")

while (continua):

    #Se si è loggati come Admin
    if mio_admin.auth == True:
        print("________________________________________________________________")
        print("[ADMIN CONTROL PANEL]")
        print("[1] Crea conto. [2] Elimina conto. [3] Visualizza tutti i conti.")
        print("________________________________________________________________")
    



    #Chiedo in input all'utente l'operazione
    operazione = input("Seleziona un operazione da fare: ")
    
    if operazione == '1' and mio_admin.auth == True:
        mio_admin.add_conto()
    elif operazione == '1':
        mio_conto.deposito()
    elif operazione == '2':
        mio_conto.prelievo()
    elif operazione == '3' and mio_admin.auth == True:
        mio_admin.view_conti()
    elif operazione == '3':
        print(mio_conto.informazioni())
    elif operazione == '4':
        mio_conto.stampa_saldo()
    elif operazione == '5':
        mio_conto.visualizza_transazioni()
    elif operazione == '6':
        admin_login()
    else:
        print("Grazie e arrivederci!")
        continua = False


