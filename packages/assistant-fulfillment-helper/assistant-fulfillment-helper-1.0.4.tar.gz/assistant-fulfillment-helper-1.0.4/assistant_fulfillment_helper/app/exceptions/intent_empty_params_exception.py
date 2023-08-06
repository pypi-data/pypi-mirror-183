class IntentEmptyParamException(Exception):
    """Exception raised for register intent with empty params.

    Attributes:
        empty_param -- param name that is empty
    """

    def __init__(self, empty_param):
        message = f"O parâmetro '{empty_param}' deve ter um conteúdo válido para registrar uma intenção (intent)"
        self.message = message
        super().__init__(self.message)

    