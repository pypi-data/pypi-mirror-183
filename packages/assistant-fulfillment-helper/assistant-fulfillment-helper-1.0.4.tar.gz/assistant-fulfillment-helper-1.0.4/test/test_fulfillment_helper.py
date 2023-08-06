from mock import MagicMock
from test.mocks import constants
from assistant_fulfillment_helper.fulfillment_helper import FulfillmentHelper
from assistant_fulfillment_helper.app.responses.fulfillment_helper_response import FulfillmentHelperResponse
from assistant_fulfillment_helper.app.controllers.fulfillment_intent import FulfillmentIntent
from assistant_fulfillment_helper.app.controllers.fulfillment_server import FulfillmentServer

my_test_callback = MagicMock(return_value = FulfillmentHelperResponse(message='ok'))
FulfillmentServer.run = MagicMock()

class TestFulfillmentHelper:

    def test_resgister_intent_success(self):
        node_name = 'test_resgister_intent_success'
        fh = FulfillmentHelper()
        intent_data = dict(
            node_name = node_name,
            webhook_token = constants.FAKE_TOKEN,
            callback = my_test_callback
        )
        fh.registerIntent(
            node_name=intent_data['node_name'],
            callback=intent_data['callback'],
            webhook_token=intent_data['webhook_token']
        )
        assert intent_data == FulfillmentIntent.get(
            intent_data['node_name'],
            intent_data['webhook_token']
        )

    def test_start_server(self):
        fh = FulfillmentHelper()
        assert fh.start(
            debug=True,
            host="123.456.789.012",
            port=1000
        ) == None # None == no errors
