class ResumeParsingError(Exception):
    def __init__(self, message="Failed to parse resume"):
        self.message = message
        super().__init__(self.message)
