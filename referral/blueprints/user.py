"""
    This is the blueprint for handling the user's data. Should keep avaiable here
"""
from sanic.response import json
from sanic import Blueprint
from referral.util import any_none, formatting
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

    return json(stmt)
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

    return json(stmt)
    
@user_bp.route('/register', methods=["POST", "OPTIONS"])
async def user_register(request):
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    confirm = request.json.get("confirm", None)
    referrer = request.json.get("referrer", None)
    first = request.json.get("first", None)
    last = request.json.get("last", None)
    
    should_continue = any_none([email, password, confirm, first, last])
    if should_continue == False:
        wrong = formatting(400, "You're not giving us all of the necessary data", {})
        return json(wrong, status=wrong['status'])
    
    stmt = user_db.register(email, password, confirm, referrer, first, last)

    return json(stmt)
