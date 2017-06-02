from flask import Flask
from src.models.organization import Organization_Model


def postOrganizations(session, organization_model):
    print(organization_model.name)
    try:
        print(organization_model.created_at)
        session.add(organization_model)
        session.commit()
        return True
    except:
        print('name')
        return False


def getOrganizations(session):
    return session.query(Organization_Model).all()
