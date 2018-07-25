from referral.util import any_none, referral_hash
from faker import Faker
fake = Faker()

def test_checks():
    not_type = any_none("shaklshka")
    a_none = any_none([None, "sahjksh"])
    no_none = any_none(["shajksa", "shajksa"])

    assert not_type == False
    assert a_none == False
    assert no_none == True


def test_referral_hash():
    email = fake.email()
    user_hash = referral_hash(email)
    assert user_hash is not None
    assert isinstance(user_hash, str)