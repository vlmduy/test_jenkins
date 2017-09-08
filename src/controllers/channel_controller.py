"""
src/controllers/channel_controller.py: Channel Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import request, jsonify, Blueprint, abort
from src.models.channel import Channel_Model
from src.daos.channel_dao import insert_channel_from_db, \
        find_channel_from_db, get_channel_by_id, remove_channel_by_id, \
        edit_channel_by_id
from src.daos.login_dao import verify_token
from src.controllers.handler_error import error_handler, not_loggin
import db

channel_api = Blueprint('channel_api', __name__)


@channel_api.route('/channel', methods=['GET'])
def find_all_channel():
    """
    API find channel from channel_dao
    :return: channels
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception as ex:
        print ex
        return not_loggin()

    with db.session() as session:
        result = find_channel_from_db(session)
        # data_all = [product.serialize() for product in channel]
        return jsonify(result)


@channel_api.route('/channel/id/<channel_id>', methods=['GET'])
def find_channel_by_id(channel_id):
    """
    API find channel by channel_id from channel_dao
    :return: channel
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    with db.session() as session:
        channel = get_channel_by_id(channel_id, session)
        result = channel.serialize()
        return jsonify(result)


@channel_api.route('/channel', methods=['POST'])
def insert_channel():
    """
    API insert channel from channel_dao
    :parameter: json
    :return: channel
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()


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
        _result = insert_channel_from_db(session, channel)
        return jsonify(_result)


@channel_api.route('/channel/<channel_id>', methods=['DELETE'])
def remove_channel(channel_id):
    """
    API remove channel by channel_id from channel_dao
    :return: channel
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

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
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

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
        _result = edit_channel_by_id(session, _channel)
        return jsonify(_result)
