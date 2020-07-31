from flask import request, Blueprint, jsonify
from ..models import User, Product, Postagem
from flask_jwt_extended import jwt_required
from ..extensions import db


postagem_api = Blueprint('postagem_api', __name__)


@postagem_api.route('/postagens/post/', methods=['POST'])
@jwt_required
def create_post():

    data = request.json

    product_id = data.get('product_id')
    caption = data.get('caption')
    img_url = 'url/#' #implementar serviço de armazenamento de imagem

    if not data or not caption or not product_id:
        return {'error': 'algum dado faltando no body'}, 400

    postagem = Postagem(caption=caption, img_url=img_url, product_id=product_id)

    db.session.add(postagem)
    db.session.commit()

    return postagem.json(), 201