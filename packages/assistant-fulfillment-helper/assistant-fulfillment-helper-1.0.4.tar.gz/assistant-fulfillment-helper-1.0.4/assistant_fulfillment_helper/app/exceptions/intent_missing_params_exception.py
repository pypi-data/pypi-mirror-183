class IntentMissingParamException(Exception):
    """Exception raised for register intent with missing params.

    Attributes:
        missing_param -- param name that is missing
    """

    def __init__(self, missing_param):
        message = f"O parâmetro '{missing_param}' é obrigatório para registrar uma Intenção (intent)"
        self.message = message
        super().__init__(self.message)

    