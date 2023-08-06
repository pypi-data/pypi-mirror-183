import json
import pytest
from test.mocks import constants
from assistant_fulfillment_helper.fulfillment_helper import FulfillmentHelper
from assistant_fulfillment_helper.app.responses.fulfillment_helper_response import FulfillmentHelperResponse

class TestWebhookRequest:

    def test_health_check_success(self, client):
        response = client.get('/')
        assert response.json == dict(
            message = "This is a TOTVS Assistant Webhook. See https://pypi.org/project/assistant-fulfillment-helper/ for more details"
        )

    def test_webhook_request_unauthenticated(self, client):
        response = client.post('/')
        assert response.json == dict(
            message = 'Authorization, or X-Auth-Key and X-Auth-ConnectorId is invalid. Please authenticate.'
        )

    def test_webhook_request_missing_params(self, client):
        response = client.post('/', 
            headers={'X-Assistant-Signature-Token' : constants.FAKE_TOKEN}
        )
        assert response.status_code == 422
        assert list(response.json.keys()).sort() == list(constants.FAKE_PARAMS.keys()).sort()

    def test_webhook_request_to_an_undefined_intent(self, client):
        response = client.post('/', 
            headers={'X-Assistant-Signature-Token' : constants.FAKE_TOKEN},
            data=json.dumps(constants.FAKE_PARAMS),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.json == dict(
            error = f"Nenhum callback foi encontrado para a intenção '{constants.FAKE_PARAMS['intent_name']}'",
            exception = 'IntentCallbackNotFoundException'
        )

    def test_webhook_request_using_an_invalid_token(self, client):
        def my_test_callback(p):
            return

        fh = FulfillmentHelper()
        fh.registerIntent(
            callback=my_test_callback,
            webhook_token="invalid token",
            node_name=constants.FAKE_PARAMS['intent_name']
        )
        response = client.post('/', 
            headers={'X-Assistant-Signature-Token' : constants.FAKE_TOKEN},
            data=json.dumps(constants.FAKE_PARAMS),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.json == dict(
            error = f"Error while calling a callback: Token inválido para o Webhook da intenção '{constants.FAKE_PARAMS['intent_name']}'.",
        )

    def test_webhook_request_with_an_invalid_response(self, client):
        def my_test_callback(p):
            return

        intent_name = 'test_webhook_request_with_an_invalid_response'

        fh = FulfillmentHelper()
        fh.registerIntent(
            callback=my_test_callback,
            webhook_token=constants.FAKE_TOKEN,
            node_name=intent_name
        )
        params = constants.FAKE_PARAMS
        params['intent_name'] = intent_name
        response = client.post('/', 
            headers={'X-Assistant-Signature-Token' : constants.FAKE_TOKEN},
            data=json.dumps(constants.FAKE_PARAMS),
            content_type='application/json'
        )
        assert response.status_code == 400
        assert response.json == dict(
            error = f"O callback 'my_test_callback' deve retornar uma classe do tipo 'FulfillmentHelperResponse'",
            exception = 'IntentResponseInstanceException'
        )

    def test_webhook_request_with_a_valid_response(self, client):
        def my_test_callback(p):
            return FulfillmentHelperResponse(
                message="Test message"
            )

        intent_name = 'test_webhook_request_with_a_valid_response'

        fh = FulfillmentHelper()
        fh.registerIntent(
            callback=my_test_callback,
            webhook_token=constants.FAKE_TOKEN,
            node_name=intent_name
        )
        params = constants.FAKE_PARAMS
        params['intent_name'] = intent_name
        response = client.post('/', 
            headers={'X-Assistant-Signature-Token' : constants.FAKE_TOKEN},
            data=json.dumps(constants.FAKE_PARAMS),
            content_type='application/json'
        )
        assert response.status_code == 200
        assert response.json == dict(
            jump_to= None, 
            logout= False,
            message= 'Test message',
            options= None,
            parameters= None,
            short_message= None
        )