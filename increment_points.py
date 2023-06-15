import redis
import sys

r = redis.Redis(
  host='redis-12114.c293.eu-central-1-1.ec2.cloud.redislabs.com',
  port=12114,
  password='3FYHn60i42mOmITHT7CnlJI4SoYyoX4P'
  )

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