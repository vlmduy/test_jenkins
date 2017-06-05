"""
src/daos/channel_dao.py: Channel Dao
Copyright 2017-2018 LinhHo Training.
"""

from src.models.channel import Channel_Model
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


def insert_channel_from_db(session, channel_model):
    """
    Insert channel into database
    :parameter: session, channel
    :return: status
    """
    # Check if channel already exist in database
    result = {
        'message': 'ok',
        'status': 'ok'
    }
    _channel = get_channel_by_id(channel_id=channel_model.id, session=session)
    if _channel is None:
        try:
            session.add(channel_model)
            session.commit()
            result['message'] = 'added new channel success'
            result['status'] = 'ok'
        except Exception as ex:
            print ex
            result['message'] = 'added new channel fail'
            result['status'] = 'ok'
    else:
        try:
            session.merge(channel_model)
            session.commit()
            print "Merged channel %s", channel_model
            result['message'] = 'edited new channel success'
            result['status'] = 'ok'
        except Exception as ex:
            print "Error on merge channel %s. Exception: %s", channel_model, ex
            session.rollback()
            result['message'] = 'edited new channel fail'
            result['status'] = 'ok'
    return result


def find_channel_from_db(session):
    """
    Find channel from database
    :parameter: session
    :return: channel
    """
    return session.query(Channel_Model).all()


def get_channel_by_id(channel_id, session):
    """
    Get channel by channel_id
    :param ochannel_id: channel id
    :type channel_id: integer
    :param session: database connection session
    :type session:
    :rtype: <channel object> or None
    """
    try:
        query = session.query(Channel_Model).filter(Channel_Model.id == channel_id)
        channel = query.one()
        return channel
    except MultipleResultsFound as ex:
        print "Multiple results found Organization.get_channel_by_id %s", ex
        return query.first()
    except NoResultFound as ex:
        print "No result found Organization.get_channel_by_id %s", ex
        return None
