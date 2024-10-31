from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant.db"
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    availability = db.Column(db.Boolean, default=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    items = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), default="Pending")

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Welcome to the Restaurant Menu & Order Management System"

@app.route("/menu", methods=["GET"])
def get_menu():
    menu_items = MenuItem.query.all()
    return jsonify([{
        "id": item.id,
        "name": item.name,
        "price": item.price,
        "description": item.description,
        "availability": item.availability
    } for item in menu_items])

@app.route("/menu", methods=["POST"])
def add_menu_item():
    data = request.get_json()
    new_item = MenuItem(
        name=data["name"],
        price=data["price"],
        description=data.get("description"),
        availability=data.get("availability", True)
    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Menu item added successfully!"})

@app.route("/menu/<int:item_id>", methods=["PUT"])
def update_menu_item(item_id):
    data = request.get_json()
    menu_item = MenuItem.query.get(item_id)
    if not menu_item:
        return jsonify({"error": "Menu item not found"}), 404

    if "name" in data:
        menu_item.name = data["name"]
    if "price" in data:
        menu_item.price = data["price"]
    if "description" in data:
        menu_item.description = data["description"]
    if "availability" in data:
        menu_item.availability = data["availability"]

    db.session.commit()
    return jsonify({"message": "Menu item updated successfully!"})

@app.route("/orders", methods=["POST"])
def place_order():
    data = request.get_json()
    new_order = Order(
        customer_name=data["customer_name"],
        items=",".join(str(item_id) for item_id in data["items"])
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!", "order_id": new_order.id})

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        "id": order.id,
        "customer_name": order.customer_name,
        "items": order.items,
        "status": order.status
    } for order in orders])

@app.route("/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    data = request.get_json()
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if "status" in data:
        order.status = data["status"]
    if "customer_name" in data:
        order.customer_name = data["customer_name"]

    db.session.commit()
    return jsonify({"message": "Order updated successfully!"})

# Add the route to render the order form
@app.route('/order')
def order_form():
    return render_template('order_form.html')

@app.route('/view_orders')
def view_orders():
    return render_template('view_orders.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
