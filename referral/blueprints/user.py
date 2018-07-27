"""
    This is the blueprint for handling the user's data. Should keep avaiable here
"""
from sanic.response import json
from sanic import Blueprint
from referral.util import any_none, formatting, which_none
from referral.database import User

user_db = User()

user_bp = Blueprint('user', url_prefix="/user")


@user_bp.route('/', methods=["POST", "OPTIONS"])
async def bp_root(request):
    return json({'msg': 'This is pretty darn basic'})

@user_bp.route('/info', methods=["POST", "OPTIONS"])
async def user_info(request):
    email = request.json.get("email", None)
    should_continue = any_none([email])
    
    if should_continue == False:
        wrong = formatting(400, "You're not giving us all of the necessary data", {})
        return json(wrong, status=wrong['status'])
    
    stmt = user_db.get_user_info(email)

    return json(stmt, status=stmt['status'])
    # return json({'my': 'blueprint'})


@user_bp.route('/login', methods=["POST", "OPTIONS"])
async def user_login(request):
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    should_continue = any_none([email, password])
    if should_continue == False:
        wrong = formatting(400, "You're not giving us all of the necessary data", {})

        return json(wrong, status=wrong['status'])
    
    stmt = user_db.login(email, password)

    return json(stmt, status=stmt['status'])



    
@user_bp.route('/register', methods=["POST", "OPTIONS"])
async def user_register(request):
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    confirm = request.json.get("confirm", None)
    referrer = request.json.get("referrer", None)
    first = request.json.get("first", None)
    last = request.json.get("last", None)
    ip = request.json.get("ip", None)
    
    # Make sure to collect the public IP from the client
    should_continue = any_none([email, password, confirm, first, last, ip])
    if should_continue == False:
        missing = which_none({
            "email": email,
            "password": password,
            "confirm": confirm,
            "first": first,
            "last": last,
            "ip": ip
        })
        
        wrong = formatting(400, "You're not giving us all of the necessary data", {"missing": missing})
        return json(wrong, status=wrong['status'])
    stmt = user_db.register(email, password, confirm, referrer, first, last, ip)

    return json(stmt, status=stmt['status'])




@user_bp.route('/pay', methods=["POST", "OPTIONS"])
async def user_pay(request):
    email = request.json.get("email", None)
    payment_token = request.json.get("token", None)
    
    # Get the token for python
    # Charge the user and update in the db that the user bought
    # stmt = user_db.login(email, password)

    return json({}, status=200)