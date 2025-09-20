from flask import Flask


# Create a Flask application instance

app = Flask(__name__)


# Route for the home page

@app.route("/")

def home():

# Message asking user to enter a number in the URL

 return "Please add a number to the URL, like /5 or /10"


# Route that accepts an integer from the URL

@app.route("/<int:number>")

def prime(number):

 primes = "" 

# Loop through all numbers from 2 to 'number'

 for i in range(2, number + 1):

  for n in range(2, (i // 2) + 1):

   if i % n == 0:
       break
   else:
    primes += str(i) + ", "

 return primes

if __name__ == '__main__':
  app.run(debug=True,port=5001)