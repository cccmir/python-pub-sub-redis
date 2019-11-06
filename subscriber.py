from redis import Redis

rClient = Redis()
pubSub = rClient.pubsub(ignore_subscribe_messages=True)
try:
    res = pubSub.subscribe('channel')
    for item in pubSub.listen():
        print(item['data'].decode('utf-8'))
except Exception as ex:
    print(str(ex))
finally:
    pubSub.close()
    rClient.close()