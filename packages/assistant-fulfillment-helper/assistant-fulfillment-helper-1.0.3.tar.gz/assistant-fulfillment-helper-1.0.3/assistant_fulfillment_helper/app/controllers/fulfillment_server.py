from assistant_fulfillment_helper.server import application

class FulfillmentServer:

    def run(self, _host, _port, _debug):
        application.run(
            host=_host, 
            port=_port, 
            debug=_debug
        )

