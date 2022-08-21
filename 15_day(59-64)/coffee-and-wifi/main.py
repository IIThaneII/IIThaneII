from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class MyDataRequired(DataRequired):
    field_flags = ()

class URLRequired(URL):
    field_flags = ()

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[MyDataRequired()])
    location = StringField('Cafe Location on Google Map (URL)', validators=[MyDataRequired(), URLRequired()])
    open_time = StringField('Opening time e.g. 8AM', validators=[MyDataRequired()])
    close_time = StringField('Closing time e.g. 5:30PM', validators=[MyDataRequired()])
    coffee_rate = SelectField('Coffee Rating', choices=['✘','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️'])
    wifi_rate = SelectField('Wifi Strength Rating', choices=['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'])
    power_rate = SelectField('Power Socket Availability', choices=['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee_rate.data},"
                           f"{form.wifi_rate.data},"
                           f"{form.power_rate.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf8", newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
