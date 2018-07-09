from referral.util import any_none
def test_checks():
    not_type = any_none("shaklshka")
    a_none = any_none([None, "sahjksh"])
    no_none = any_none(["shajksa", "shajksa"])

    assert not_type == False
    assert a_none == False
    assert no_none == True