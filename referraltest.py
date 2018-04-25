from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from createreferraltables import Base, Referral

engine = create_engine('sqlite:///referrals.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Insert a Person in the person table
referral = Referral(email='kah.kevin.hill@gmail.com')
session.add(referral)
session.commit()


referral_two = Referral(email='kivo360', referred_by=referral.uid)
session.add(referral_two)
session.commit()

# Insert an Address in the address table
