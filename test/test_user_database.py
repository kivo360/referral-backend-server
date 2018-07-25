from referral.database import User, hash_pass
from contextlib import suppress
import crayons as cy
from faker import Faker
fake = Faker()

userlib = User()


original_user_email = "kevin@ymail.com"
original_user_password = "samplePassword"
other_pass = "otherPassword"
referr_email_list = [
    "kivo@pmail.com",
    "kevin@imcool.im",
    "jack@people.com",
    "shit@dick.com"
]

referr_email_list_second_level = [
    "kivo@gmail.com",
    "kevin@hecool.im",
    "jack@wecool.com",
    "shit@mecool.com"
]


referr_email_list_third_level = [
    "kivo@bmail.com",
    "kevin@bmail.com",
    "jack@bmail.com",
    "shit@bmail.com"
]

def test_remove_all_test_users():
    userlib.admin_remove(original_user_email)

def test_create_user():
    """ 
        Tests:
            - Create user with incorrect email formatt
            - Create user with incorrect confirm password
            - Create user with valid information
            - Create user that already exist 
    """
    wrongEmail = "kevinymail"
    password = "samplePassword"
    wrongPassword = "amplePassword"
    first = "Kevin"
    last = "Hill"

    ipaddress = fake.ipv4_public(network=False, address_class=None)
    # fake.ipv4_public(network=False, address_class=None)

    incorrect_email = userlib.register(wrongEmail, password, password, None, first, last,ipaddress)
    incorrect_confirm = userlib.register(original_user_email, password, wrongPassword, None, first, last, ipaddress)
    valid_user = userlib.register(original_user_email, original_user_password, original_user_password, None, first, last, ipaddress)
    should_exist = userlib.register(original_user_email, original_user_password, original_user_password, None, first, last, ipaddress)

    assert incorrect_email["status"] == 400
    assert incorrect_confirm["status"] == 400
    assert valid_user["status"] in [200, 202]
    assert should_exist["status"] in [200, 202]
    
    print(cy.red("Test User Registration", bold=True), end="\n")
    print_line()
    print(incorrect_confirm)
    print(incorrect_email)
    print(valid_user)
    print(should_exist)
    print("\n")


def test_user_login():
    wrongEmail = "kevingmail.com"
    wrongPassword = "wrongPassword"
    nonExistent = "kevin@gmail.com"
    

    wrong_email_format = userlib.login(wrongEmail, "myPassword")
    wrong_password = userlib.login(original_user_email, wrongPassword)
    non_existent = userlib.login(nonExistent, wrong_password)
    exist_user = userlib.login(original_user_email, original_user_password)
    


    print(cy.yellow("Test User Login", bold=True), end="\n")
    print_line()
    print(wrong_email_format)
    print(wrong_password)
    print(non_existent)
    print(exist_user)
    print("\n")

    

    assert wrong_email_format["status"] == 400
    assert wrong_password["status"] == 401
    assert non_existent["status"] in [400, 401]
    assert exist_user["status"] == 200
    



def test_add_referrals():
    first = "Kevin"
    last = "Hill"
    
    referrer_hash = "936f55cef131d54d769dea223b480e8707c76dd8eff1f37b8a758012181f646d6baf535ee9bf01c4c642a7e246bd01157f9b2ce1feb58ae989c01b56a52a8f01"
    print(cy.green("First Level Referral", bold=True), end="\n")
    print_line()
    for uemail in referr_email_list:
        ipaddress = fake.ipv4_public(network=False, address_class=None)
        valid_user = userlib.register(uemail, other_pass, other_pass, referrer_hash, first, last, ipaddress)
        print(valid_user)
        assert valid_user["status"] in [200, 202]

    print()

    print(cy.cyan("Second Level Referral", bold=True))
    print_line()
    nreferrer_user = hash_pass(referr_email_list[0])
    for sec_lvl in referr_email_list_second_level:
        ipaddress = fake.ipv4_public(network=False, address_class=None)
        valid_user = userlib.register(sec_lvl, other_pass, other_pass, nreferrer_user, first, last, ipaddress)
        print(valid_user)
        assert valid_user["status"] in [200, 202]
    

    print()
    print(cy.blue("Third Level Referral", bold=True))
    print_line()
    nreferrer_user_2 = hash_pass(referr_email_list_second_level[0])
    for third_lvl in referr_email_list_third_level:
        ipaddress = fake.ipv4_public(network=False, address_class=None)
        valid_user = userlib.register(third_lvl, other_pass, other_pass, nreferrer_user_2, first, last, ipaddress)
        print(valid_user)
        assert valid_user["status"] in [200, 202]


def test_get_referred():
    print("\n")
    print(cy.magenta("Referred Users", bold=True))
    print_line()
    ref_list = userlib.get_user_info(original_user_email)
    print(ref_list)
    pass


def print_line():
    print("------------------------------------------------------------------------")

    # assert True == True
# Create User without correct confirm password
# Create User with correct confirm password
# Create User that already exist
    # Should return 400 status
# Create User without correct email format
    # Should return 400 status


# Refer user (create user with referred)

# Get users referred by first user
    # Should return status 200
    # Should have list length of 1

# Add another user referred by first user
    # Should return status 200

# Get users referred by first user
    # Should return status 200
    # Should get a list of 2


# Add user referred by second user
    # Should return status 200

# Get users referred by first user
    # Should return status 200
    # Should return list length of 3
    # Should return 


# assert True == True
# assert "user" == "user"