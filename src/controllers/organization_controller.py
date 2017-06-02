from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.organization import Organization_Model
from src.daos.organization_dao import postOrganizations, getOrganizations
from flask import Blueprint
import db 

organization_api = Blueprint('organization_api', __name__)

@organization_api.route('/organizations', methods=['GET'])
def getOrganization():
    with db.session() as session:
      data = getOrganizations(session) #fetch all products on the table

      data_all = [[product.id, product.name] for product in data]
      return jsonify(products=data_all)

@organization_api.route('/organizations', methods=['POST'])
def createOrganization():
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

    organization = Organization_Model(id, name, logo, primary_contact_email, status, details, created_at, updated_at) #prepare query statement

    if postOrganizations(session, organization):
      print(organization.created_at)
      # organization_id = organization.id #fetch last inserted id
      # data = Organization_Model.query.filter_by(id=organization_id).first() #fetch our inserted product

      # result = [data.name, data.id] #prepare visual data
      return jsonify(session=organization)
    else:
      message = {
            'message': 'fail',
      }
      resp = jsonify(message)
      return resp

if __name__ == '__main__':
    app.debug = True
    app.run()