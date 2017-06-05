"""
src/models/organization.py: Organization Mapping Object
Copyright 2017-2018 LinhHo Training.
"""

from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from db import Base


class Organization_Model(Base):
    __tablename__ = 'organizations'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    logo = Column(String(120), unique=True)
    primary_contact_email = Column(String(120), unique=True)
    status = Column(Boolean, unique=True)
    details = Column(String(120), unique=True)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    def __init__(self,
                 id,
                 name,
                 logo,
                 primary_contact_email,
                 status,
                 details,
                 created_at,
                 updated_at):
        self.id = id
        self.name = name
        self.logo = logo
        self.primary_contact_email = primary_contact_email
        self.status = status
        self.details = details
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return '<Name %r>' % self.name
