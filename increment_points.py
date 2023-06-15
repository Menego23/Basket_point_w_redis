#funzione per incrementare i numeri in una partita di basket
def incrementa_punti_squadra(squadra, punti):
    try:
        if punti >= 1 and punti <= 3:
            r.incrby(f"punti_squadra_{squadra}", punti)
        else:
            print("Il numero di punti deve essere compreso tra 1 e 3")
    except Exception as e:
        print(e, "\nSquadra non valida")
