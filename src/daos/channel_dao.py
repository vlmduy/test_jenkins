"""
src/daos/channel_dao.py: Channel Dao
Copyright 2017-2018 LinhHo Training.
"""

from datetime import datetime
import pytz
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
        'channel': None,
        'message': 'ok',
        'status': 'ok'
    }
    _channel = get_channel_by_name(channel_name=channel_model.name, session=session)
    if _channel is None:
        try:
            channel_model.created_at = datetime.utcnow().replace(tzinfo=pytz.UTC)
            session.add(channel_model)
            session.commit()
            result['message'] = 'added new Channel success'
            result['status'] = 'ok'
            result['channel'] = channel_model
        except Exception as ex:
            session.rollback()
            result['message'] = 'added new Channel fail'
            result['status'] = 'error'
    else:
        result['message'] = 'Channel already exists'
        result['status'] = 'error'
    return result


def edit_channel_by_id(session, channel_model):
    """
    Edit channel into database
    :parameter: session, channel
    :return: status
    """
    # Check if channel already exist in database
    result = {
        'message': 'ok',
        'channel': None,
        'status': 'ok'
    }
    _channel = get_channel_by_id(channel_id=channel_model.id, session=session)
    if _channel is None:
        result['message'] = 'channel does not exist'
        result['status'] = 'error'
    else:
        try:
            channel_model.created_at = _channel.created_at
            channel_model.updated_at = datetime.utcnow().replace(tzinfo=pytz.UTC)
            session.merge(channel_model)
            session.commit()
            result['message'] = 'edited channel success'
            result['status'] = 'ok'
            result['channel'] = channel_model
        except Exception as ex:
            print ex
            session.rollback()
            result['message'] = 'edited channel fail'
            result['status'] = 'error'
    return result


def remove_channel_by_id(session, channel_id):
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
    _channel = get_channel_by_id(channel_id=channel_id, session=session)
    if _channel is None:
        result['message'] = 'channel not exist'
        result['status'] = 'fail'
    else:
        try:
            session.delete(_channel)
            session.commit()
            result['message'] = 'removed channel success'
            result['status'] = 'ok'
        except Exception as ex:
            session.rollback()
            result['message'] = 'removed channel fail'
            result['status'] = 'fail'
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


def get_channel_by_name(channel_name, session):
    """
    Get channel by channel_name
    :param ochannel_name: channel name
    :type channel_name: strin
    :param session: database connection session
    :type session:
    :rtype: <channel object> or None
    """
    try:
        query = session.query(Channel_Model).filter(Channel_Model.name == channel_name)
        channel = query.one()
        return channel
    except MultipleResultsFound as ex:
        print "Multiple results found Organization.get_channel_by_name %s", ex
        return query.first()
    except NoResultFound as ex:
        print "No result found Organization.get_channel_by_name %s", ex
        return None
