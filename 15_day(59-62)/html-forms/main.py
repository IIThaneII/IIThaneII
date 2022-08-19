from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST"])
def receive_data():
    if request.method == "POST":
       # getting input with name = username in HTML form
       name = request.form.get("username")
       # getting input with name = userpassword in HTML form
       password = request.form.get("userpassword")
       return f'<h1>Name: {name}, Password: {password}</h1>'

if __name__ == '__main__':
    app.run(debug=True)