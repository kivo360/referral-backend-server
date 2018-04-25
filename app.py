from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS, cross_origin
from sanic_limiter import Limiter, get_remote_address
from refer_file import add_user_with_filters
import sys

app = Sanic()
CORS(app)


limiter = Limiter(app, global_limits=['5 per hour', '10 per day'], key_func=get_remote_address)


def get_request_userip(request):
    return request.json.get('user_ip', '')


@app.route("/check", methods=["POST"]):
    test_cookie = request.cookies.get('check')

@app.route("/register", methods=["POST"])
@limiter.limit("4/minute", key_func=get_request_userip)
@limiter.limit("15/hour", key_func=get_request_userip)
async def test(request):
    if request.json is None:
        return json({'msg': 'Not sending in anything'})
    user_ip = request.json.get('user_ip', None)
    email = request.json.get('email', None)
    referred_by = request.json.get('referer', None)

    if user_ip is None:
        return json({'msg': "User Ip Address isn't here"});
    
    if email is None:
        return json({'msg': "Email doesn't exist"})    
    
    val = add_user_with_filters(email, referred_by)
    return json(val)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)



