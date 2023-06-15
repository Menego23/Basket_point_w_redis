import redis
import sys

r = redis.Redis(
  host='redis-12114.c293.eu-central-1-1.ec2.cloud.redislabs.com',
  port=12114,
  password='3FYHn60i42mOmITHT7CnlJI4SoYyoX4P'
  )


# funzione per incrementare i numeri in una partita di basket
def incrementa_punti_squadra(squadra, punti):
    try:
        if punti >= 1 and punti <= 3:
            r.incrby(f"punti_squadra_{squadra}", punti)
        else:
            print("Il numero di punti deve essere compreso tra 1 e 3")
    except TypeError:
        print("Squadra non valida")


# funzione per ottenere i punti di una squadra
def get_points(squadra):
    try:
        points = int(r.get(f"punti_squadra_{squadra}"))
        return points
    except TypeError:
        print("Squadra non valida\nScegliere squadra 'A' o 'B'")


# funzione per stampare il vincitore
def stampa_vincitore():
    a = get_points("A")
    b = get_points("B")
    if a > b:
        return("Vince la squadra A")
    elif a < b:
        return("Vince la squadra B")
    else:
        return("Pareggio")
