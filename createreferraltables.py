import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from hashids import Hashids
hashids = Hashids()

Base = declarative_base()
import os
import binascii

class Referral(Base):
    __tablename__ = 'Refer'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    uid = Column(String, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    referral_code = Column(String(250), nullable=True)
    referred_by = Column(String, nullable=True)
    
    def __init__(self, email, referred_by=None):
        # hasher = hashlib.sha1(str(uuid.uuid4()))
        self.uid = str(uuid.uuid4())
        self.email = email
        self.referral_code = binascii.b2a_hex(os.urandom(5))
        self.referred_by = referred_by
        


# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///referrals.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
