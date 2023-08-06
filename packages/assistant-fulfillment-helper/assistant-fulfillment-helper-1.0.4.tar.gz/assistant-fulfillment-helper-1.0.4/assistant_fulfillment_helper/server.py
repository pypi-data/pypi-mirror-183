from assistant_fulfillment_helper.app import create_app
from flask_cors import CORS

application = create_app()
CORS(application)