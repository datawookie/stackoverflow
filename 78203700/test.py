import redis

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

print(r.hgetall("1"))

r.set("test", "123")
print(r.get("test"))
