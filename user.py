from flask import Flask
app=Flask('__name__')

@app.route('/<username>')
def show(username):
    return f"Hi {username}"+"<a href='/leon'>anythgdsuidny</a>"


if __name__=='__main__':
    app.run()