class IacerException(Exception):
    """Raised when iacer experiences a fatal error"""


class InvalidActionError(IacerException):
    """Exception raised for error when invalid action is supplied

    Attributes:
        expression -- input expression in which the error occurred
    """

    def __init__(self, expression):
        self.expression = expression
        super().__init__()
