from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
db.create_all()

@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe={
        #Omit the id from the response
        # "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        
        #Put some properties in a sub-category
        "amenities": {
          "seats": random_cafe.seats,
          "has_toilet": random_cafe.has_toilet,
          "has_wifi": random_cafe.has_wifi,
          "has_sockets": random_cafe.has_sockets,
          "can_take_calls": random_cafe.can_take_calls,
          "coffee_price": random_cafe.coffee_price,
        }
    })

@app.route("/all")
def all():
    cafes = db.session.query(Cafe).all()
    cafe_list = []
    for cafe in cafes:
        cafe_dict = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url,
                     "img_url": cafe.img_url,
                     "location": cafe.location, "has_sockets": cafe.has_sockets,
                     "has_toilet": cafe.has_toilet, "has_wifi": cafe.has_wifi,
                     "can_take_calls": cafe.can_take_calls, "seats": cafe.seats,
                     "coffee_price": cafe.coffee_price}
        cafe_list.append(cafe_dict)
    all_cafes = {"cafes": cafe_list}
    all_cafes_json = jsonify(cafes=all_cafes["cafes"])
    return all_cafes_json

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=query_location).all()
    if cafes:
        cafe_list = []
        for cafe in cafes:
            cafe_dict = {"id": cafe.id, "name": cafe.name, "map_url": cafe.map_url,
                        "img_url": cafe.img_url,
                        "location": cafe.location, "has_sockets": cafe.has_sockets,
                        "has_toilet": cafe.has_toilet, "has_wifi": cafe.has_wifi,
                        "can_take_calls": cafe.can_take_calls, "seats": cafe.seats,
                        "coffee_price": cafe.coffee_price}
            cafe_list.append(cafe_dict)
        all_cafes = {"cafes": cafe_list}
        all_cafes_json = jsonify(cafes=all_cafes["cafes"])
        return all_cafes_json
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
    )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added new cafe."})
    return jsonify(response={"error": "Unable to add new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()  
        return jsonify(response={"success": "Successfully updated new cafe."})
    return jsonify(Error={"Not Found": "Sorry a cafe with that id was not found."})


## HTTP DELETE - Delete Record
top_secret_api_key = "hehe"
@app.route("/delete-price/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    cafe_to_delete = Cafe.query.get(cafe_id)
    if request.args.get("api_key") != top_secret_api_key:
        return jsonify(Error={"error": "Make sure you have the correct api_key."})
    elif cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})
    return jsonify(Error={"Not Found": "Sorry a cafe with that id was not found."})


if __name__ == '__main__':
    app.run(debug=True)
