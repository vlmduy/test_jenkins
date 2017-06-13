"""
src/controllers/channel_controller.py: Channel Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import request, jsonify, Blueprint, abort
from src.models.channel import Channel_Model
from src.daos.channel_dao import insert_channel_from_db, \
        find_channel_from_db, get_channel_by_id, remove_channel_by_id, \
        edit_channel_by_id
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
    if not request.json:
        abort(400)
    else:
        try:
            id = None
            name = request.get_json(silent=True)['name']
            owner = request.get_json(silent=True)['owner']
            org_id = request.get_json(silent=True)['org_id']
            is_private = request.get_json(silent=True)['is_private']
            state = request.get_json(silent=True)['state']
            status = request.get_json(silent=True)['status']
            shared_with = request.get_json(silent=True)['shared_with']
            created_at = None
            updated_at = None
        except Exception as ex:
            return error_handler(ex)

    channel = Channel_Model(id, name, owner, org_id, is_private,
                            state, status, shared_with, created_at, updated_at)
    with db.session() as session:
        _message = insert_channel_from_db(session, channel)
        if _message['status'] == 'error':
            return error_handler(_message['message'])
        else:
            _channel = _message['channel']
            return jsonify(_channel.serialize())


@channel_api.route('/channel/<channel_id>', methods=['DELETE'])
def remove_channel(channel_id):
    """
    API remove channel by channel_id from channel_dao
    :return: channel
    """
    with db.session() as session:
        message = remove_channel_by_id(session, channel_id)
        return jsonify(message)


@channel_api.route('/channel/<channel_id>', methods=['PUT'])
def edit_channel(channel_id):
    """
    API edit channel from channel_dao
    :parameter: json
    :return: channel
    """
    if not request.json:
        abort(400)
    else:
        try:
            id = channel_id
            name = request.get_json(silent=True)['name']
            owner = request.get_json(silent=True)['owner']
            org_id = request.get_json(silent=True)['org_id']
            is_private = request.get_json(silent=True)['is_private']
            state = request.get_json(silent=True)['state']
            status = request.get_json(silent=True)['status']
            shared_with = request.get_json(silent=True)['shared_with']
            created_at = None
            updated_at = None
        except Exception as ex:
            return error_handler(ex)

    _channel = Channel_Model(id, name, owner, org_id, is_private,
                            state, status, shared_with, created_at, updated_at)

    with db.session() as session:
        _message = edit_channel_by_id(session, _channel)
        if _message['status'] == 'error':
            return error_handler(_message['message'])
        else:
            _result = _message['channel']
            return jsonify(_result.serialize())


@channel_api.errorhandler(500)
def error_handler(error):
    """
    Handler error 500
    :return: Request Error url
    """
    _error = str(error)
    message = {
        'status': 500,
        'message': _error
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp
