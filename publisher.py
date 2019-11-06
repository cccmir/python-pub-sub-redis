from redis import Redis

rClient = Redis()
try:
    while True:
        msg = input("Send Message to subscriber: ")
        rClient.publish('channel', msg )
        print()
except:
    pass
finally:
    rClient.close()