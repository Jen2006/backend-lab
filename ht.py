from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Welcome!</h1>
        <p>This is a simple HTML page in Flask.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)