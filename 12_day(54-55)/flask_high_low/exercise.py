from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapped_func():
        bold = f"<b>{function()}</b>"
        return bold
    return wrapped_func

def make_emphasize(function):
    def wrapped_func():
        emphasize = f"<em>{function()}</em>"
        return emphasize
    return wrapped_func

def make_underline(function):
    def wrapped_func():
        underline = f"<u>{function()}</u>"
        return underline
    return wrapped_func

@app.route('/bye')
@make_bold
@make_underline
@make_emphasize
def say_bye(): # http://127.0.0.1:5000/bye
    return 'Bye!' 

if __name__ == '__main__':
    app.run(debug=True)