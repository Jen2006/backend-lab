#generate 10 numbers
from flask import Flask
app=Flask(__name__)

@app.route('/')
def natural():
    lst=[]
    for i in range(1,11):
        lst.append(i)
    return lst


if __name__=='__main__':
     app.run()

