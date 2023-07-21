# Definisco la classe 'Conto'
class Conto:

    # Costruttore
    def __init__(self, saldo, proprietario):
        self.saldo = saldo
        self.proprietario = proprietario
        self.transaction_counter = 0
        self.transactions = []

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



#Definisco la classe Admin
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auth = False
        
        #Methods









# MAIN PROGRAM 


#METHODS
def admin_login():
    username = input("Inserisci username dell'admin:\n ")
    password = input("Inserisci password:\n")

    #Controllo username e password che corrispondano
    if (username == "admin" and mio_admin.username == "admin") and (password == mio_admin.password and mio_admin.password == "test"):
        print(f"Bentornato {mio_admin.username}!")
    else:
        print("Username o password errati!")




#ISTANZE
mio_conto = Conto(50, "Lorenzo Moccia")
mio_admin = Admin("admin", "test")


# Imposto una variabile a True per fare un loop infinito del programma.
continua = True


#MENU
print("Benvenuto nel Bank-Account software!")
print("\n")
print("[1] Deposito.\n[2] Prelievo.\n[3] Informazioni.\n[4] Saldo.\n[5] Visualizza storico transazioni.\n[6] Admin Control Panel ")

while (continua):

    #Chiedo in input all'utente l'operazione
    operazione = input("Seleziona un operazione da fare: ")
    
    if operazione == '1':
        mio_conto.deposito()
    elif operazione == '2':
        mio_conto.prelievo()
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



#if
#else
#else if