from flask import Flask 

app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"The sum of {a} and {b} is {a + b}"

if __name__ == '__main__':
    app.run()


