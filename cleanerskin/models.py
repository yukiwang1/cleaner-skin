from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask import app
from cleanerskin import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


user_favorite_products = db.Table(
    "user_favorite_products",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    favorites = db.relationship(
        "Product",
        secondary=user_favorite_products,
        backref=db.backref("favorited_by"),
        lazy=True,
    )

    # expiration time 30 min
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(1000), nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default="default.jpg")
    name = db.Column(db.String(2000), nullable=False)
    ingredients = db.Column(db.String(50000), nullable=False)
    category = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"Product('{self.brand}', '{self.name}')"


class BadIngredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(1000), nullable=False)
    uses = db.Column(db.String(1000), nullable=False)
    reason = db.Column(db.String(5000), nullable=False)
    resources = db.Column(db.String(1000), nullable=False)
    names = db.Column(db.String(5000), nullable=False)
    risk_level = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"BadIngredients('{self.category}')"

    def __lt__(self, other):
        # Return True if this is less than other
        if self.risk_level == other.risk_level:
            return self.category > other.category
        if self.risk_level == "Low" and other.risk_level == "Moderate":
            return True
        if self.risk_level == "Low" and other.risk_level == "High":
            return True
        if self.risk_level == "Moderate" and other.risk_level == "High":
            return True
        return False


class SafeIngredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f"SafeIngredients('{self.names}')"
