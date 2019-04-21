class Rule:

    verification_method = None

    message = ''

    message_type = ''

    def __init__(self, verification_method, message:str, message_type:str):
        self.verification_method = verification_method