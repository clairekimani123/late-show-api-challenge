from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db
from server.models.episode import Episode
from server.models.appearance import Appearance

bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': ep.id,
        'date': ep.date.isoformat(),
        'number': ep.number
    } for ep in episodes]), 200

@bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    appearances = [{
        'id': app.id,
        'rating': app.rating,
        'guest': {
            'id': app.guest.id,
            'name': app.guest.name,
            'occupation': app.guest.occupation
        }
    } for app in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date.isoformat(),
        'number': episode.number,
        'appearances': appearances
    }), 200

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted successfully'}), 200