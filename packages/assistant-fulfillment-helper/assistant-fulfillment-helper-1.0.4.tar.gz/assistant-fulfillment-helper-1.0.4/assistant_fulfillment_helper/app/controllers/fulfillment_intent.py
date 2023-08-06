from assistant_fulfillment_helper.app.exceptions.duplicated_intent_node_exception import DuplicatedIntentNodeException
from assistant_fulfillment_helper.app.exceptions.intent_empty_params_exception import IntentEmptyParamException
from assistant_fulfillment_helper.app.exceptions.intent_missing_params_exception import IntentMissingParamException
from assistant_fulfillment_helper.app.exceptions.intent_invalid_callback_exception import IntentInvalidCallbackException
from assistant_fulfillment_helper.app.exceptions.intent_callback_not_found_exception import IntentCallbackNotFoundException
from assistant_fulfillment_helper.app.exceptions.invalid_webhook_token_exception import InvalidWebhookTokenException

class FulfillmentIntent:

    __intents = []

    @staticmethod
    def __validate_intent(intent_data:dict):
        """
            Check if this intent is valid
        """
        mandatory_params = [
            'callback', 
            'webhook_token',
            'node_name'
        ]

        for param in mandatory_params:
            if param not in intent_data:
                raise IntentMissingParamException(param)
            if intent_data[param] == False or intent_data[param] == '':
                raise IntentEmptyParamException(param)
            if param == 'callback' and callable(intent_data[param]) == False:
                raise IntentInvalidCallbackException(intent_data['node_name'])
        FulfillmentIntent.__intent_node_exists(intent_data)

    @staticmethod
    def __intent_node_exists(intent_node:dict):
        """
            Check if this intent is duplicated
        """
        for intent in FulfillmentIntent.__intents:
            if intent['node_name'] == intent_node['node_name']:
                raise DuplicatedIntentNodeException(intent['node_name'])

    @staticmethod
    def define(intent_data:dict):
        """
            Define a new intent to the intents list
        """
        FulfillmentIntent.__validate_intent(intent_data)
        FulfillmentIntent.__intents.append(intent_data)

    @staticmethod
    def get(intent_name:str, webhook_token:str):
        """
            Get a intent by name
        """
        for intent in FulfillmentIntent.__intents:
            if intent['node_name'] == intent_name:
                if intent['webhook_token'] == webhook_token:
                    return intent
                raise InvalidWebhookTokenException(intent_name)
        raise IntentCallbackNotFoundException(intent_name)
