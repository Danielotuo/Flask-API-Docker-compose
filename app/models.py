from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    """
    Represents a product in the database.
    """
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def serialize(self):
        """
        Serializes the product object into a dictionary.
        """
        return {
            'id': self.id,
            'name': self.name,
            'price': str(self.price)
        }
