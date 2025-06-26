from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db
from server.models.appearance import Appearance

bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    if not data or not data.get('rating') or not data.get('guest_id') or not data.get('episode_id'):
        return jsonify({'error': 'Rating, guest_id and episode_id required'}), 400
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'guest_id': appearance.guest_id,
            'episode_id': appearance.episode_id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400