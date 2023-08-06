import logging
from flask import Blueprint, jsonify, request
from webargs import fields
from webargs.flaskparser import parser
from .auth_helper import error_authentication_message
from functools import wraps
from assistant_fulfillment_helper.app.controllers.fulfillment_intent import FulfillmentIntent
from assistant_fulfillment_helper.app.responses.fulfillment_helper_response import FulfillmentHelperResponse
from assistant_fulfillment_helper.app.exceptions.intent_response_instance_exception import IntentResponseInstanceException
from assistant_fulfillment_helper.app.exceptions.intent_callback_not_found_exception import IntentCallbackNotFoundException

# Logger
logger = logging.getLogger(__name__)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s: %(message)s")
console.setFormatter(formatter)
logger.addHandler(console)

server_bp = Blueprint('main', __name__)

logger.info('Pronto. O app está preparado para receber novas requisições.')

@server_bp.route('/', methods=['GET'])
def index():
    return {
        'message': 'This is a TOTVS Assistant Webhook. See https://pypi.org/project/assistant-fulfillment-helper/ for more details'
    }, 200

# We want to validate if the consumer is authorize to access some of our endpoints. Because of that we created this decorator.
# It validates if the information sent in the authorization header is valid in Carol.
# If you want your endpoint to be validated you just need to add @requires_auth before the method's name of that endpoint.
def requires_auth(f):
    '''
    Determine if the access token is valid in Carol.
    It returns an error message with 401 status code in case the token is not valid.
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        headers = request.headers
        auth = request.authorization
        if not headers and not auth:
            return error_authentication_message()
        elif not headers.get('X-Assistant-Signature-Token'):
            return error_authentication_message()
        return f(*args, **kwargs)
    return decorated

@server_bp.route('/', methods=['POST'])
@requires_auth
def webhook_call():
    """
    Rota que efetivamente deve ser chamada nas configurações de webhook. O código trata dinâmicamente
    as requisições, decidindo qual código a ser usado para o tratamento baseado no nó em execução re-
    cebido no payload. O tratamento das requisições segue a documentação do backend disponível no link
    abaixo:
        - https://tdn.totvs.com/pages/releaseview.action?pageId=682036247
    """
    
    results = dict()

    # Try to parse threshold as a dict on the first attempt
    query_arg = {
        "intent_name": fields.Str(required=True, description='The node being processed.'),
        "parameters": fields.Dict(required=True, description='All the context parameters.'),
        "sessionLog": fields.List(fields.Dict(), required=True, description='Logs up to the current point.'),
        "namedQueries": fields.Dict(required=False, missing={}, description='named query results, if any.'),
        "query": fields.Str(required=True, description='The node being processed.'),
        "message": fields.Str(required=True, description='The node being processed.'),
        "language": fields.Str(required=False, missing="", description='The node being processed.'),
        "allRequiredParamsPresent": fields.Bool(required=False, missing=True),
        "carolOrganization": fields.Str(required=True, description='Carol organization name.'),
        "carolEnvironment": fields.Str(required=True, description='Carol tenant name.'),
        "carolOrganizationId": fields.Str(required=True, description='Carol organization id.'),
        "carolEnvironmentId": fields.Str(required=True, description='Carol tenant id.'),
        "sessionId": fields.Str(required=True, description='The current conversation session.'),
        "isProduction": fields.Bool(required=False, missing=False),
        "channelName": fields.Str(required=True, description='the channel which the message is comming from.')
    }

    # Executa o parser dos argumentos e já instância o objeto correto para o processamento da mensagem
    args = parser.parse(query_arg, request)

    try:
        # Obtém e valida a intent
        intent = FulfillmentIntent.get(
            args.get('intent_name'),
            request.headers.get("X-Assistant-Signature-Token")
        )

        # Chama o callback registrada na intent
        results = intent['callback'](args)
        if isinstance(results, FulfillmentHelperResponse) == False:
            raise IntentResponseInstanceException(intent['callback'].__name__)
        return dict(
            message = results.message,
            short_message = results.short_message,
            jump_to = results.jump_to,
            options = results.options,
            logout = results.logout,
            parameters = results.parameters
        )
    except (
        IntentResponseInstanceException, 
        IntentCallbackNotFoundException
    ) as e: 
        results = dict(
            exception = type(e).__name__,
            error = e.args[0]
        )
    except Exception as e: 
        results = dict(error = f"Error while calling a callback: {e}.")

    logger.error(results)
    return results, 400

@server_bp.errorhandler(422)
@server_bp.errorhandler(400)
def handle_error(err):
    headers = err.data.get("headers", None)
    messages = err.data.get("messages", ["Invalid request."])
    messages = messages.get('json', messages)
    if headers:
        return jsonify(messages), err.code, headers
    else:
        return jsonify(messages), err.code