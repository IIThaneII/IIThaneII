from flask import Flask, render_template
import requests

URL_GENDER = "https://api.genderize.io"
URL_AGE = "https://api.agify.io"

app = Flask(__name__)

@app.route('/')
def home():
    return  '<h1>HI THIS IS OUR HOMEPAGE.</h1>' \
            '<h1>PLEASE INPUT YOUR NAME.</h1>' \
            '<img src="https://media.giphy.com/media/YAlhwn67KT76E/giphy.gif" width=400>'

@app.route('/<name>')
def name_input(name):
    params = {
    'name': name
}
    response = requests.get(url=URL_GENDER, params=params)
    response.raise_for_status()
    gender_result = response.json()
    gender = gender_result['gender']
    response = requests.get(url=URL_AGE, params=params)
    response.raise_for_status()
    age_result = response.json()
    age = age_result['age']
    return render_template('index.html', name=name, gender=gender, age=age)


if __name__ == '__main__':
    app.run(debug=True)