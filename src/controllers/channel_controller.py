from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.channel import Channel_Model
from src.daos.channel_dao import postChannels, getChannels
from flask import Blueprint
import db 

channel_api = Blueprint('channel_api', __name__)

@channel_api.route('/channels', methods=['GET'])
def getChannels():
    with db.session() as session:
      channel = getOrganizations(session) #fetch all products on the table

      data_all = [[product.id, product.name] for product in channel]
      return jsonify(products=data_all)

@channel_api.route('/channels', methods=['POST'])
def createChannels():
  with db.session() as session:
    # fetch pram from the request
    id = request.get_json()['id']
    name = request.get_json()['name']
    logo = request.get_json()['logo']
    primary_contact_email = request.get_json()['primary_contact_email']
    status = request.get_json()['status']
    details = request.get_json()['details']
    created_at = request.get_json()['created_at']
    updated_at = request.get_json()['updated_at']
    created_at = None
    updated_at = None

    channel = Channel_Model(id, name, owner, org_id, is_private, state, status, jsonb, created_at, updated_at) #prepare query statement

    if postOrganizations(session, channel):
      print(channel.created_at)
      return jsonify(session=result)
    else:
      message = {
            'message': 'fail',
      }
      resp = jsonify(message)
      return resp

if __name__ == '__main__':
    app.debug = True
    app.run()