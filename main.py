import sys
import redis
import functions as f

r = redis.Redis(
  host='redis-12114.c293.eu-central-1-1.ec2.cloud.redislabs.com',
  port=12114,
  password='3FYHn60i42mOmITHT7CnlJI4SoYyoX4P'
  )

is_connected = r.ping()

if not is_connected:
    print("Error: could not connect to Redis")
    sys.exit(-1)
print("Connected to Redis")


# test funzioni
f.incrementa_punti_squadra("A", 1)
f.incrementa_punti_squadra("B", 3)
print(f.get_points("A"))
print(f.get_points("B"))
print(f.stampa_vincitore())
