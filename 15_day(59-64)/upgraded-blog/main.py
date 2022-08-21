from flask import Flask, render_template, request
from post import Post
import requests
import smtplib

my_email = "nguyennam2741@yahoo.com"
my_password = "G-5*EqpY!mLrijH"

posts = requests.get("https://api.npoint.io/06aad41aa3ab34cfa126").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["date"], post["image"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', all_posts=post_objects)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("get_post.html", post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posts')
def posts():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/form-data", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        data = request.form
        send_message(data)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_message(data):
    people_message = f"Blog Message\n\nName: {data['name']}\nPhone: {data['phone_num']}\nMessage: \n{data['message']}"
    if "yahoo" in data["email"]:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=data["email"], password=my_password)
            connection.sendmail(from_addr=data["email"], to_addrs="ntguppy13@gmail.com", msg=people_message)
    else:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=data["email"], password=my_password)
            connection.sendmail(from_addr=data["email"], to_addrs="ntguppy13@gmail.com", msg=people_message)


if __name__ == '__main__':
    app.run(debug=True)