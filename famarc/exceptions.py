class FamarcBaseException(Exception):
    pass

class IdDoesNotExist(FamarcBaseException):
    def __init__(self, object_class, id):
        self.object_class = object_class
        self.id = id
    def __str__(self):
        return 'The {} with id {} does not exist.'.format(
               self.object_class.__name__, self.id)

class BadId(FamarcBaseException):
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return '"{}" is not a valid id.'.format(self.id)
