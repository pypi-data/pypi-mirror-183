class IntentInvalidCallbackException(Exception):
    """Exception raised when a declared callback is not callable.

    Attributes:
        node_name -- name of the noda that has a not callable callback
    """

    def __init__(self, node_name):
        message = f"A intenção '{node_name}' possui um callback inválido"
        self.message = message
        super().__init__(self.message)

    