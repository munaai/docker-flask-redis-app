import redis
from flask import Flask

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    return f'Welcome to my page!'

@app.route('/count')
def count():
# Increment the visit count in redis
    r.incr('visit_count')
    visit_count = r.get('visit_count').decode('utf-8')
    return f'You have now been here {visit_count} times!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)