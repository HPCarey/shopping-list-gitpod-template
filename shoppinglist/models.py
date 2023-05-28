from shoppinglist import db


class List(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    list_name = db.Column(db.String(50), unique=True, nullable=False)
    items = db.relationship("Item", backref="list", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.list_name


class Item(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey("list.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Item: {1}".format(
            self.id, self.item_name
        )
