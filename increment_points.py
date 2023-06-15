#funzione per incrementare i numeri in una partita di basket
def incrementa_punti_squadra(squadra, punti):
    if squadra == "A":
        if punti >= 1 and punti <= 3:
            r.incrby("punti_squadra_A", punti)
        else:
            print("Il numero di punti deve essere compreso tra 1 e 3")
    elif squadra == "B":
        if punti >= 1 and punti <= 3:
            r.incrby("punti_squadra_B", punti)
        else:
            print("Il numero di punti deve essere compreso tra 1 e 3")
    else:
        print("Squadra non valida")