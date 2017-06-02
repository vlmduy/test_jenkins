from flask import Flask
from src.models.channel import Channel_Model


def insert_channel_from_db(session, channel_model):
    """
    Insert channel into database
    :parameter: session, channel
    :return: status
    """
    print(channel_model.name)
    try:
        print channel_model.created_at
        session.add(channel_model)
        session.commit()
        return True
    except:
        print('name')
        return False


def find_channel_from_db(session):
    """
    Find channel from database
    :parameter: session
    :return: channel
    """
    return session.query(Channel_Model).all()
