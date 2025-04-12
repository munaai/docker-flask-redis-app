import redis
from flask import Flask, send_from_directory

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello_world():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                background-color: #f0f8ff;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: #ff6f61;
                font-size: 36px;
            }
            p {
                font-size: 18px;
                color: #555;
            }
            a {
                text-decoration: none;
                color: #ff6f61;
                font-weight: bold;
            }
            a:hover {
                color: #ff9a8b;
            }
            img {
                max-width: 200px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to Muna's Count App!</h1>
        <p>Visit the <a href="/count">count page</a> to see how many times you've visited.</p>
        <img src="/static/image.png" alt="Hourglass Icon">
    </body>
    </html>
    """
    return html

@app.route('/count')
def count():
    # Increment the visit count in Redis
    r.incr('visit_count')
    visit_count = r.get('visit_count').decode('utf-8')

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Visit Count</title>
        <style>
            body {{
                background-color: #f0f8ff;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }}
            h1 {{
                color: #ff6f61;
                font-size: 36px;
            }}
            p {{
                font-size: 18px;
                color: #555;
            }}
            a {{
                text-decoration: none;
                color: #ff6f61;
                font-weight: bold;
            }}
            a:hover {{
                color: #ff9a8b;
            }}
            img {{
                max-width: 200px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>You have now been here {visit_count} times!</h1>
        <p>Go back to the <a href="/">home page</a>.</p>
        <img src="/static/image.png" alt="Hourglass Icon">
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
