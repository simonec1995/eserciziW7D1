#importiamo librerie preimpostate di python
import random # serve per generare numeri o fare scelte casuali
import string # contiene costanti utili come tutte le lettere o i numeri
#definiamo la funzione 
def gen_psw():
    print("\n Benvenuto in Generatore di password\n")
    print("\nPuoi scegliere tra due livelli di complessità\n")
#prepariamo dei set di caratteri che sommiamo per generare delle password
    ascii_chars = string.digits + string.ascii_letters + string.punctuation
    alphanum_chars = string.digits + string.ascii_letters
  # creo un ciclo di controllo, questo serve a fare in modo che una volta creata la password il programma ricominci a meno che non si decida di uscire  
    while True:
         scelta = input("Scegli S se vuoi una password semplice o C se vuoi una password complessa: ").upper() #uso upper per prevenire errori maiscolo\minuscolo
#dentro if definisco la psw complessa, definisco la lunghezza in caratteri e do il tipo che ho creato sopra grazie alle librerie che ho importato
         if scelta == "C":
     
             lunghezza = 20
             tipo = ascii_chars
             break
         elif scelta == "S": #dentro elif definisco le psw semplici
             
             lunghezza = 8
             tipo = alphanum_chars
             break
         else : #uso else per prevenire errori di battitura
             print("Devi scegliere tra S oppure C")

    psw = "" #preparo il 'cntenitore' vuoto della password
    counter = 0 #definisce che la password parte da 0 caratteri

    while counter < lunghezza:
        char = random.choice(tipo) #pesca un carattere a caso dal set scelto (semplice o complesso)
        psw += char #lo aggiunge al 'contenitore vuoto'
        counter += 1 #aggiunge 1 per ogni carattere fino a fermarsi alla lunghezza stabilita (8 o 20)

    print(f"la password generata è: {psw}") #stampa a video la password
#questa di fatto è la funzione principale richiama la funzione che ho definito in gen_psw e si occupa di far ricominciare o terminare il programma in base alla scelta dell' utilizzatore 
while True:
     gen_psw() 

     ripetere = input("\n Vuoi generare un' altra password? (s/n): "). lower() #lower fa lo stesso lavoro di upper ma al contrario
     if ripetere != "s":
         print("Arrivederci!")
         break
#### avrei potuto riproporre il concetto di if-elif-else per fare scegliere solo s o n, invece di fatto in questo modo qualunche cosa si prema che non sia s o S il programma terminerà


