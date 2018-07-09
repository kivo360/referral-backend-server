from sanic import Sanic, Blueprint
from referral.blueprints.user import user_bp
from sanic.response import json
from sanic_cors import CORS, cross_origin
from sanic_limiter import Limiter, get_remote_address
# from refer_file import add_user_with_filters, go_through_network
import sys

app = Sanic(__name__)
CORS(app)


limiter = Limiter(app, global_limits=['100 per hour', '15 per minute'])

app.blueprint(user_bp)

# user_bp = Blueprint("user", url_prefix="/user")


# def get_request_userip(request):
#     return request.json.get('user_ip', '')


# @limiter.limit("1000 per hour;15/minute")
# @user_bp.route("/info", methods=["POST", "OPTIONS"])
# async def get_user(request):
#     if request.json is None:
#         return json({'msg': 'Not sending in anything'})


#     user_ip = request.json.get('user_ip', None)
#     email = request.json.get('email', None)


#     if user_ip is None:
#         return json({'msg': "User Ip address isn't here."});


#     if email is None:
#         return json({'msg': "Email isn't here."});

#     # val = go_through_network(email)
#     return json({"msg": "Test"})


# @limiter.limit("1000 per hour;15/minute")
# @user_bp.route("/login", methods=["POST", "OPTIONS"])
# async def login(request):
#     if request.json is None:
#         return json({'msg': 'Not sending in anything'})


#     user_ip = request.json.get('user_ip', None)
#     email = request.json.get('email', None)


#     if user_ip is None:
#         return json({'msg': "User Ip address isn't here."});


#     if email is None:
#         return json({'msg': "Email isn't here."});

#     # val = go_through_network(email)
#     return json({"msg": "Test"})


# @limiter.limit("1000 per hour;15/minute")
# @user_bp.route("/register", methods=["POST", "OPTIONS"])
# async def test(request):
#     if request.json is None:
#         return json({'msg': 'Not sending in anything'})
#     user_ip = request.json.get('user_ip', None)
#     email = request.json.get('email', None)
#     referred_by = request.args.get('ref', None)
#     print(referred_by, file=sys.stderr)
#     if user_ip is None:
#         return json({'msg': "User Ip Address isn't here"});
    
#     if email is None:
#         return json({'msg': "Email doesn't exist"})    

#     return json({"msg": "Test"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)



