"""
src/daos/organization_dao.py: Organization Dao
Copyright 2017-2018 LinhHo Training.
"""

from src.models.organization import Organization_Model
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def insert_organization_to_db(session, organization_model):
    """
    Insert organization into database
    :parameter: session, organization
    :return: status
    """
    # Check if organization already exist in database
    result = {
        'message': 'ok',
        'status': 'ok'
    }
    _org = get_organization_by_id(organization_id=organization_model.id, session=session)
    if _org is None:
        try:
            session.add(organization_model)
            session.commit()
            result['message'] = 'added new organization success'
            result['status'] = 'ok'
        except Exception as ex:
            print "Error on add organization %s. Exception: %s", organization_model, ex
            session.rollback()
            rresult['message'] = 'added new organization success'
            result['status'] = 'ok'
    else:
        try:
            session.merge(organization_model)
            session.commit()
            print "Merged organization %s", organization_model
            result['message'] = 'edited new organization success'
            result['status'] = 'ok'
        except Exception as ex:
            print "Error on merge organization %s. Exception: %s", organization_model, ex
            session.rollback()
            result['message'] = 'edited new organization success'
            result['status'] = 'ok'
    return result


def find_organization_from_db(session):
    """
    Find organization from database
    :parameter: session
    :return: organization
    """
    return session.query(Organization_Model).all()


def get_organization_by_id(organization_id, session):
    """
    Get organization by organization_id
    :param organization_id: organization id
    :type organization_id: integer
    :param session: database connection session
    :type session:
    :rtype: <organization object> or None
    """
    try:
        query = session.query(Organization_Model).filter(Organization_Model.id == organization_id)
        organization = query.one()
        return organization
    except MultipleResultsFound as ex:
        print "Multiple results found Organization.get_organization_by_id %s", ex
        return query.first()
    except NoResultFound as ex:
        print "No result found Organization.get_organization_by_id %s", ex
        return None
