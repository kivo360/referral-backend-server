from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from email_validator import validate_email, EmailNotValidError





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




# Insert an Address in the address table


def add_user_with_filters(laemail, refer=None):
    current_user = session.query(Referral).filter(
        Referral.email == laemail).first()

    if current_user is not None:
        return {
            'success': False,
            'referral_code': None,
            'reason': 'email',
            'msg': "That email already exist."
        }
    try:
        v = validate_email(laemail)  # validate and get info
        laemail = v["email"]  # replace with normalized form


    except EmailNotValidError:
        # email is not valid, exception message is human-readable
        return {
            'success': False,
            'referral_code': None,
            'reason': 400,
            'msg': "That email is invalid. Please try again."
        }

    if refer is None:
        referral = Referral(email=laemail)
        try:
            session.add(referral)
            session.commit()
            return {
                'success': True,
                'msg': 'Successfully added email. Here is your referral code',
                'referral_code': referral.referral_code
            }
        except Exception:
            session.rollback()
            return {
                'success': False,
                'msg': 'Did not add due to our problem',
                'reason': 500
            }
    elif refer is not None:
        ref = session.query(Referral).filter(
            Referral.referral_code == refer).first()
        if ref is None:
            try:
                referral = Referral(email=laemail)
                session.add(referral)
                session.commit()
                return {
                    'success': True,
                    'msg': 'Successfully added email. Here is your referral code',
                    'referral_code': referral.referral_code
                }
            except Exception:
                session.rollback()
                return {
                    'success': False,
                    'msg': 'Wasn\'t able to add referral code',
                    'reason': 'us'
                }
        else:
            try:
                referral = Referral(email=laemail, referred_by=refer)
                session.add(referral)
                session.commit()
                return {
                    'success': True,
                    'msg': 'successfully added email. Here is your referral code',
                    'referral_code': referral.referral_code
                }
            except Exception:
                session.rollback()
                return {
                    'success': False,
                    'msg': 'Wasn\'t able to add referral code',
                    'reason': 'us'
                }
        



# address.post_code
