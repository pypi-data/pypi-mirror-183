import pytest
from mock import MagicMock
from test.mocks import constants
from assistant_fulfillment_helper.app.controllers.fulfillment_intent import FulfillmentIntent
from assistant_fulfillment_helper.app.responses.fulfillment_helper_response import FulfillmentHelperResponse
from assistant_fulfillment_helper.app.exceptions.invalid_webhook_token_exception import InvalidWebhookTokenException
from assistant_fulfillment_helper.app.exceptions.duplicated_intent_node_exception import DuplicatedIntentNodeException
from assistant_fulfillment_helper.app.exceptions.intent_invalid_callback_exception import IntentInvalidCallbackException
from assistant_fulfillment_helper.app.exceptions.intent_empty_params_exception import IntentEmptyParamException
from assistant_fulfillment_helper.app.exceptions.intent_missing_params_exception import IntentMissingParamException
from assistant_fulfillment_helper.app.exceptions.intent_callback_not_found_exception import IntentCallbackNotFoundException

my_test_callback = MagicMock(return_value = FulfillmentHelperResponse(message='ok'))

class TestFulfillmentIntent:

    def test_register_node_missing_node_name(self):
        with pytest.raises(IntentMissingParamException) as e_info:
            FulfillmentIntent.define(dict(
                webhook_token = constants.FAKE_TOKEN,
                callback = my_test_callback
            ))
        assert e_info.value.args[0] == f"O parâmetro 'node_name' é obrigatório para registrar uma Intenção (intent)"


    def test_register_node_missing_webhook_token(self):
        node_name = 'test_register_node_missing_webhook_token'
        with pytest.raises(IntentMissingParamException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                callback = my_test_callback
            ))
        assert e_info.value.args[0] == f"O parâmetro 'webhook_token' é obrigatório para registrar uma Intenção (intent)"

    def test_register_node_missing_callback_function(self):
        node_name = 'test_register_node_missing_callback_function'
        with pytest.raises(IntentMissingParamException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                webhook_token = constants.FAKE_TOKEN
            ))
        assert e_info.value.args[0] == f"O parâmetro 'callback' é obrigatório para registrar uma Intenção (intent)"

    def test_register_node_empty_node_name(self):
        node_name = ''
        with pytest.raises(IntentEmptyParamException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                webhook_token = constants.FAKE_TOKEN,
                callback = my_test_callback
            ))
        assert e_info.value.args[0] == "O parâmetro 'node_name' deve ter um conteúdo válido para registrar uma intenção (intent)"

    def test_register_node_empty_webhook_token(self):
        node_name = 'test_register_node_empty_webhook_token'
        with pytest.raises(IntentEmptyParamException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                webhook_token = '',
                callback = my_test_callback
            ))
        assert e_info.value.args[0] == "O parâmetro 'webhook_token' deve ter um conteúdo válido para registrar uma intenção (intent)"

    def test_register_node_empty_callback_function(self):
        node_name = 'test_register_node_empty_callback_function'
        with pytest.raises(IntentEmptyParamException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                webhook_token = constants.FAKE_TOKEN,
                callback = ''
            ))
        assert e_info.value.args[0] == "O parâmetro 'callback' deve ter um conteúdo válido para registrar uma intenção (intent)"

    def test_register_node_with_an_uncallable_callback(self):
        node_name = 'test_register_node_with_an_uncallable_callback'
        with pytest.raises(IntentInvalidCallbackException) as e_info:
            FulfillmentIntent.define(dict(
                node_name = node_name,
                webhook_token = constants.FAKE_TOKEN,
                callback = 'my_callback'
            ))
        assert e_info.value.args[0] == f"A intenção '{node_name}' possui um callback inválido"

    def test_register_duplicated_node_name(self):
        node_name = 'test_register_node_with_an_uncallable_callback'
        intent_data = dict(
            node_name = node_name,
            webhook_token = constants.FAKE_TOKEN,
            callback = my_test_callback
        )
        FulfillmentIntent.define(intent_data)

        with pytest.raises(DuplicatedIntentNodeException) as e_info:
            FulfillmentIntent.define(intent_data)
        assert e_info.value.args[0] == f"A intenção '{node_name}' já está em uso"

    def test_get_intent_node_not_found(self):
        node_name = 'test_get_intent_node_not_found'
        with pytest.raises(IntentCallbackNotFoundException) as e_info:
            FulfillmentIntent.get(
                node_name,
                constants.FAKE_TOKEN
            )
        assert e_info.value.args[0] == f"Nenhum callback foi encontrado para a intenção '{node_name}'"

    def test_get_intent_invalid_token(self):
        node_name = 'test_get_intent_invalid_token'
        intent_data = dict(
            node_name = node_name,
            webhook_token = constants.FAKE_TOKEN,
            callback = my_test_callback
        )
        FulfillmentIntent.define(intent_data)
        with pytest.raises(InvalidWebhookTokenException) as e_info:
            FulfillmentIntent.get(
                node_name,
                'an invalid token'
            )
        assert e_info.value.args[0] == f"Token inválido para o Webhook da intenção '{node_name}'"

    def test_get_intent_success(self):
        node_name = 'test_get_intent_success'
        intent_data = dict(
            node_name = node_name,
            webhook_token = constants.FAKE_TOKEN,
            callback = my_test_callback
        )
        FulfillmentIntent.define(intent_data)
        intent_ret = FulfillmentIntent.get(node_name, constants.FAKE_TOKEN)

        assert intent_ret == intent_data

