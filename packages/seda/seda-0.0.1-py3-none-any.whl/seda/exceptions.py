class AWSError(Exception):
    pass


class ResourceDoesNotExist(AWSError):
    pass


class Conflict(AWSError):
    pass
