from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world(): # http://127.0.0.1:5000
    return  '<h1 style="text-align:center">Hello, World!</h1>' \
            '<p>This is a paraghraph</p>' \
            '<img src="https://media.giphy.com/media/K1wjOn6HImv7y/giphy.gif" width="300">' \

@app.route('/bye')
def say_bye(): # http://127.0.0.1:5000/bye
    return 'Bye!' 

@app.route('/<name>/<int:number>')
def hello_user(name, number): # http://127.0.0.1:5000/Thanh/19
    return f'Hello {name}, you are {number} years old.'

if __name__ == '__main__':
    app.run(debug=True)