import redis
import sys

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

