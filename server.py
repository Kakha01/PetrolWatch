from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', heading_text="Hello World!")


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=5000, debug=True)
    serve(app, host="0.0.0.0", port="8080")
