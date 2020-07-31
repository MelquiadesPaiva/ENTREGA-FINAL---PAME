from .extensions import db



class Postagem(db.Model):   
    
    __tablename__ = 'postagens'
    id = db.Column(db.Integer, primary_key=True)

    caption = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)


    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


    def json(self):

        return {'id': self.id,
                'caption': self.caption,
                'img_url': self.img_url,
                'product_id': self.product_id}


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    idade = db.Column(db.Integer, default=0)
    endereco = db.Column(db.String(50), nullable=False)

    password_hash = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean, default=False)

    permission = db.Column(db.String(3), nullable=False)

    #products = db.relationship('Product')
    #products = db.relationship('Postagem') 



    def json(self):
        user_json = {'id': self.id,
                     'name': self.name,
                     'email': self.email,
                     'idade': self.idade,
                     'endereco': self.endereco
                     }
        return user_json


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(10), nullable=False)


    postagens = db.relationship('Postagem', backref='produto')

    def json(self):

        return {'name': self.name,
                'desciption': self.description,
                'id': self.id,
                'price':self.price}
