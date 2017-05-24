from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.organization import Organization_Model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@192.168.210.84:5432/training'
db = SQLAlchemy(app)

def getOrganizations(organization_model):
    curr_session = db.session #open database session
    print(organization_model.name)
    try:
        curr_session.add(organization_model)
         #add prepared statment to opened session
        curr_session.commit() #commit changes
        print(organization_model.name)
        return True
    except:
        curr_session.rollback()
        curr_session.flush() # for resetting non-commited .add()
        # curr_session.close()
        return False
