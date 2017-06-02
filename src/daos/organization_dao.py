from flask import Flask
from src.models.organization import Organization_Model


def insert_organization_to_db(session, organization_model):
    """
    Insert organization into database
    :parameter: session, organization
    :return: status
    """
    print(organization_model.name)
    try:
        print organization_model.created_at
        session.add(organization_model)
        session.commit()
        return True
    except:
        print('name')
        return False


def find_organization_from_db(session):
    """
    Find organization from database
    :parameter: session
    :return: organization
    """
    return session.query(Organization_Model).all()
