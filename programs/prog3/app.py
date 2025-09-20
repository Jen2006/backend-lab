from flask import Flask

app = Flask(__name__)

def fibonacci(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

@app.route('/')
def fib():
    n = 34 # Number of Fibonacci numbers to return
    result = fibonacci(n)
    return ', '.join(str(num) for num in result)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
