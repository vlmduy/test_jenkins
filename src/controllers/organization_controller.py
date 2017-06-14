"""
src/controllers/organization_controller.py: Organization Controller
Copyright 2017-2018 LinhHo Training.
"""

from flask import request, jsonify, Blueprint, abort
from src.models.organization import Organization_Model
from src.daos.organization_dao import insert_organization_to_db, \
        find_organization_from_db, get_organization_by_id
from src.daos.login_dao import verify_token
from src.controllers.handler_error import error_handler, not_loggin
import db

organization_api = Blueprint('organization_api', __name__)


@organization_api.route('/organization', methods=['GET'])
def find_organization():
    """
    API find organization from organization_dao
    :return: organizations
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    with db.session() as session:
        organization_data = find_organization_from_db(session)
        data_all = [product.serialize() for product in organization_data]
        return jsonify(data_all)


@organization_api.route('/organization/id/<organization_id>', methods=['GET'])
def find_organization_by_id(organization_id):
    """
    API find organization by organization_id from organization_dao
    :return: organization
    """
    _token = request.headers.get('token')
    try:
        verify_token(_token)
    except Exception:
        return not_loggin()

    print organization_id
    with db.session() as session:
        organization_data = get_organization_by_id(organization_id, session)
        result = organization_data.serialize()
        return jsonify(result)


@organization_api.route('/organization', methods=['POST'])
def insert_organization():
    """
    API insert organization from organization_dao
    :parameter: json
    :return: user
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
            name = request.get_json()['name']
            logo = request.get_json()['logo']
            primary_contact_email = request.get_json()['primary_contact_email']
            status = request.get_json()['status']
            details = request.get_json()['details']
            created_at = request.get_json()['created_at']
            updated_at = request.get_json()['updated_at']
            created_at = None
            updated_at = None

            organization = Organization_Model(id,
                                              name,
                                              logo,
                                              primary_contact_email,
                                              status,
                                              details,
                                              created_at,
                                              updated_at)
        except Exception as ex:
            return error_handler(ex)

    with db.session() as session:
        result = insert_organization_to_db(session, organization)
        return jsonify(result)
