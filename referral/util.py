""" Use library here to format nested dictionary"""
import hashlib
salt = str("a6ecdd933b3842bcb467fed4073cb852")

# Put together who referred who

def referral_count(self):
    # Get first degree referral
    # Get the count of second degree referral
    # Get the count of third degree referrals
    # Get total referral count
    pass


def any_none(array_of_values):
    if not isinstance(array_of_values, list):
        return False
    
    for i in array_of_values:
        if i is None:
            return False
    
    return True


def hash_pass(password):
    password = str(password)
    hashed = hashlib.sha512((password + salt).encode('utf-8')).hexdigest()
    return hashed





def formatting(status, msg, data):
    return {
        "status": status,
        "msg": msg,
        "data": data
    }

