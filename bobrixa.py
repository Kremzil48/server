import os
from waitress import serve
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return """<html>
    Привет от приложения Flask
    <br>
    <img src="static/riana.png"
    </html>
    """


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)