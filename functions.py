import redis
import sys

r = redis.Redis(
  host='redis-12114.c293.eu-central-1-1.ec2.cloud.redislabs.com',
  port=12114,
  password='3FYHn60i42mOmITHT7CnlJI4SoYyoX4P'
  )


#funzione per incrementare i numeri in una partita di basket
def incrementa_punti_squadra(squadra, punti):
    try:
        if punti >= 1 and punti <= 3:
            r.incrby(f"punti_squadra_{squadra}", punti)
        else:
            print("Il numero di punti deve essere compreso tra 1 e 3")
    except Exception as e:
        print(e, "\nSquadra non valida")


def p_points(squadra):
    try:
        print(r.get(f"punti_squadra_{squadra}"))
    except Exception as e:
        print(e, "\nSquadra è == ad 'A' o 'B'")


#funzione per stampare il vincitore
def stampa_vincitore():
    if r.get("punti_squadra_A") > r.get("punti_squadra_B"):
        return("Ha vinto la squadra A")
    elif r.get("punti_squadra_A") < r.get("punti_squadra_B"):
        return("Ha vinto la squadra B")
    else:
        return("Pareggio")



