from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from src.models.channel import Channel_Model

def postChannels(session, channel_model):
    print(channel_model.name)
    try:
        print(channel_model.created_at)
        session.add(channel_model)
        session.commit()
         #add prepared statment to opened session
        
        return True
    except:
        print('name')
        return False

def getChannels(session):
    return session.query(Channel_Model).all()
