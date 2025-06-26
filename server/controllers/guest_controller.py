from flask import Blueprint, jsonify
from server.models import db
from server.models.guest import Guest

bp = Blueprint('guests', __name__, url_prefix='/guests')

@bp.route('/', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': guest.id,
        'name': guest.name,
        'occupation': guest.occupation
    } for guest in guests]), 200