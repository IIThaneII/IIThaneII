import random
from flask import Flask

app = Flask(__name__)

number = random.randint(0,9)

wrong_gif =[
    'https://media.giphy.com/media/hoaFB12CCE824/giphy.gif', 
    'https://media.giphy.com/media/uUvyQdPSl8dhu/giphy.gif', 
    'https://media.giphy.com/media/CM1rHbKDMH2BW/giphy.gif',
    'https://media.giphy.com/media/1KBL6Wu9anosFYzCWw/giphy.gif',
    'https://media.giphy.com/media/UIpzEC5QTvuOQ/giphy.gif',
    'https://media.giphy.com/media/XgB1iZOFFkUXbOhNXt/giphy.gif',
    'https://media.giphy.com/media/L5WQjD4p8IpO0/giphy.gif',
    'https://media.giphy.com/media/gfsQffBnuc6e096brx/giphy.gif',
    'https://media.giphy.com/media/TU76e2JHkPchG/giphy.gif'
]

@app.route('/')
def hello_world():
    return  '<h1>Guess a number between 0 and 9.</h1>' \
            '<img src="https://media.giphy.com/media/ZEfHV6pbn4Hr1XGGo3/giphy.gif" width="400">'

@app.route('/<int:guess>')
def guess_number(guess):
    if guess < number:
        return  '<h1 style="color:red">Too low, try again!</h1>' \
                f'<img src="{random.choice(wrong_gif)}" width="400">'
    elif guess > number:
        return  '<h1 style="color:purple">Too high, try again!</h1>' \
                f'<img src="{random.choice(wrong_gif)}" width="400">'
    else:
        return  '<h1 style="color:green">Bingoooooo!</h1>' \
                '<img src="https://media.giphy.com/media/pHZdGyFNp5sUXq4jp5/giphy.gif" width="400">'

if __name__ == '__main__':
    app.run(debug=True)