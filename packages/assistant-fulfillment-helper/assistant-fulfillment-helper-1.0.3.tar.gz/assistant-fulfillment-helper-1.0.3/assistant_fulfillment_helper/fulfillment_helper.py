from assistant_fulfillment_helper.app.controllers.fulfillment_server import FulfillmentServer
from assistant_fulfillment_helper.app.controllers.fulfillment_intent import FulfillmentIntent

class FulfillmentHelper(FulfillmentServer):

    def registerIntent(self, 
        callback: str,
        webhook_token: str,
        node_name: str
    ):
        """
            Register a new Intent callback for the Webhook
        """
        FulfillmentIntent.define(dict(
           callback = callback,
           webhook_token = webhook_token,
           node_name = node_name
        ))

    def start(self, host='0.0.0.0', port=5052, debug=False):
        """
            Run the Webhook server
        """
        self.run(host, port, debug)



