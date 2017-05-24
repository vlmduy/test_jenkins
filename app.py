from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.organization import Organization_Model
from src.controllers.test import account_api
from src.controllers.organization_controller import organization_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.210.84:5432/training'
db = SQLAlchemy(app)


app.register_blueprint(account_api)
app.register_blueprint(organization_api)

@app.route('/')
def index():
    return 'Hello World!'

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.errorhandler(500)
def error_handler(error=None):
    message = {
            'status': 500,
            'message': 'Request Error: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp

# @app.route('/products', methods=['GET'])
# def getProduct():  
#     data = Organization_Model.query.all() #fetch all products on the table

#     data_all = [[product.id, product.email] for product in data]
#     # list comprehension

#     # for product in data:
#     #     data_all.add([product.id, product.email]) #prepare visual data

#     return jsonify(products=data_all)

# @app.route('/product', methods=['POST'])
# def createProduct():

#     # fetch name and rate from the request
#     id = request.get_json()["id"]
#     name = request.get_json()["name"]
#     logo = request.get_json()["logo"]
#     primary_contact_email = request.get_json()["primary_contact_email"]
#     status = request.get_json()["status"]
#     details = request.get_json()["details"]
#     created_at = request.get_json()["created_at"]
#     updated_at = request.get_json()["updated_at"]

#     organization = Organization_Model(id, email, logo, primary_contact_email, status, details, created_at, updated_at) #prepare query statement

#     curr_session = db.session #open database session
#     try:
#         curr_session.add(organization)
#          #add prepared statment to opened session
#         curr_session.commit() #commit changes
#     except:
#         curr_session.rollback()
#         curr_session.flush() # for resetting non-commited .add()
#     # curr_session.close()

#     organization_id = organization.id #fetch last inserted id
#     data = Organization_Model.query.filter_by(id=organization_id).first() #fetch our inserted product

#     result = [data.email, data.id] #prepare visual data

#     return jsonify(session=result)

if __name__ == '__main__':
    app.debug = True
    app.run()