from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'
    serialize_rules =('-bakegoods.bakery')
    id = db.Column(db.Integer, primary_key=True)
    updated_at =db.Column(db.DateTime, onupdate=db.func.now())
    name= db.Column(db.String, unique=True)
    price= db.Column(db.Integer)
    baked_goods=db.relationship ('BakedGood', backref='bakeries')

    def __repr__(self):
        return f'<Bakery {self.name} price: {self.price}>'

    

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'
    serialize_rules =('-bakery.baked_goods')

    id = db.Column(db.Integer, primary_key=True)
    created_at =db.Column(db.DateTime, server_default=db.func.now())
    name= db.Column(db.String, unique=True)
    price= db.Column(db.Integer)
    bakery_id= db.Column(db.Integer, db.ForeignKey('bakeries.id'))
    

    def __repr__(self):
        return f'<Bakery ({self.id}):{self.name} was created at {self.created_at} with price {self.price}>'


    