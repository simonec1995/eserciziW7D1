

def conta_caratteri(lista_input):
# funzione madre che calcola la lunghezza delle parole
    return [len(parola) for parola in lista_input]
#ciclo while che utilizzo per creare un menu del gioco
while True:
    # con questi comandi stampo a schermo il menu
    print('\n CONTO I CARATTERI DELLE PAROLE CHE INSERISICI =)')
    print('1. Inizia a giocare')
    print('2. Esci dal gioco')
    # qui creo una variabile che chiamo scelta da utilizzare con if-elif
    scelta = input("\nScegli un' opzione (1 o 2): ")
# uso if-elif-else 
    if scelta =='1':    
         testo_utente = input('inserisci alcune parole separate da uno spazio: ')
         #split serve a dividere una stringa di testo in una lista ogni volta che trova uno spazio 
         lista_input = testo_utente.split()
         #definisco il risultato che desidero, cioè che conti i caratteri con len della lista creata con split
         risultato = conta_caratteri(lista_input)
         #scrivo a schermo
         print('la lunghezza delle parole che hai inserito è: ')
         #definisco cosa scrivere
         print(risultato)
    #uso elif per la scelta numero 2 in cui puoi uscire dal gioco, volevo che il giocatore potesse provare più volte senza dover riattivare python da terminale
    elif scelta == '2':
        print('Grazie per aver giocato! Ciao.')
        #uso break per uscire dal ciclo infinito while, se non ci fosse il programma non si chiuderebbe 
        break
    # con else prevedo l' errore di scelta nel menu del gioco
    else:
        print('Opzione non valida, per favore scegli tra 1 e 2')
