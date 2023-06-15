# funzione per stampare i punti di una squadra
import redis
import sys


def p_points(squadra):
    try:
        r.get(f"punti_squadra_{squadra}")
    except Exception as e:
        print(e, "\nSquadra è == ad 'A' o 'B'")
