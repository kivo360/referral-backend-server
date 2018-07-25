from sanic import Sanic, Blueprint
from referral.blueprints.user import user_bp
from sanic.response import json
from sanic_cors import CORS, cross_origin
from sanic_limiter import Limiter, get_remote_address
# from refer_file import add_user_with_filters, go_through_network
import sys

app = Sanic(__name__)
CORS(app, automatic_options=True)

limiter = Limiter(app, global_limits=['100 per hour', '40 per minute'])

app.static('/', './referral/static')
app.static('/', './referral/static/index.html')
app.blueprint(user_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)