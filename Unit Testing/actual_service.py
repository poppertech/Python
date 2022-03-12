import imp
from actual_repository import ActualRepository

class ActualService():
    _value = 1
    _repository:ActualRepository

    def __init__(self, repository):
        self._repository = repository

    def get_value(self):
        return self._value

    def get_repository_value(self):
        return self._repository.get_value()