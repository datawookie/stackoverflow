from flask import Flask
import redis

r = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)

print("🚨 Check for connection to Redis:")
print(r.hgetall("1"))
r.set("test", "123")
print(r.get("test"))

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=False)
