from createreferraltables import Referral, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///referrals.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
session.query(Referral).all()
ref = session.query(Referral).filter(Referral.referral_code == 'BEqHemm').first()
if ref is None:
    print("Bah Humbag")
    exit(0)
print(ref.referral_code)



# address.post_code
