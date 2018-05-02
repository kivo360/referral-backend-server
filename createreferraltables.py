import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()
import os
import binascii


class User(Base):
    __tablename__ = 'User'
    uid = Column(String, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)

    def __init__(self, email):
        self.uid = str(uuid.uuid4())
        self.email = email

class Referral(Base):
    __tablename__ = 'Refer'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    rid = Column(String, primary_key=True)
    referral_code = Column(String(250), nullable=False)
    uid = Column(String, ForeignKey("User.uid"), nullable=False)
    referred_by = Column(String, ForeignKey("User.uid"), nullable=True)
    the_count = Column(Integer, nullable=False)
    
    def __init__(self, uid, referred_by=None):
        self.rid = str(uuid.uuid4())
        self.uid = uid
        self.referral_code = binascii.b2a_hex(os.urandom(5))
        self.referred_by = referred_by
        self.the_count = 0
        



# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///referrals.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
