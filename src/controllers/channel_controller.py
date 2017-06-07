"""
src/controllers/channel_controller.py: Channel Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import request, jsonify, Blueprint
from src.models.channel import Channel_Model
from src.daos.channel_dao import insert_channel_from_db, \
        find_channel_from_db, get_channel_by_id
import db

channel_api = Blueprint('channel_api', __name__)


@channel_api.route('/channel', methods=['GET'])
def find_all_channel():
    """
    API find channel from channel_dao
    :return: channels
    """
    with db.session() as session:
        channel = find_channel_from_db(session)
        data_all = [product.serialize() for product in channel]
        return jsonify(data=data_all)


@channel_api.route('/channel/id/<channel_id>', methods=['GET'])
def find_channel_by_id(channel_id):
    """
    API find channel by channel_id from channel_dao
    :return: channel
    """
    with db.session() as session:
        channel = get_channel_by_id(channel_id, session)
        result = channel.serialize()
        return jsonify(data=result)


@channel_api.route('/channel', methods=['POST'])
def insert_channel():
    """
    API insert channel from channel_dao
    :parameter: json
    :return: channel
    """
    with db.session() as session:
        id = request.get_json()['id']
        name = request.get_json()['name']
        owner = request.get_json()['owner']
        org_id = request.get_json()['org_id']
        is_private = request.get_json()['is_private']
        state = request.get_json()['state']
        status = request.get_json()['status']
        shared_with = request.get_json()['shared_with']
        created_at = request.get_json()['created_at']
        updated_at = request.get_json()['updated_at']
        created_at = None
        updated_at = None

    channel = Channel_Model(id, name, owner, org_id, is_private,
                            state, status, shared_with, created_at, updated_at)
    message = insert_channel_from_db(session, channel)
    return jsonify(message)
