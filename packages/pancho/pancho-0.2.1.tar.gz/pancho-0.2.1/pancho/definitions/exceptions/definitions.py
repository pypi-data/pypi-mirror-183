import collections.abc


class DefinitionException(Exception):
    pass


class ActorTypeIsNotDefined(DefinitionException):
    def __init__(self, repository: str):
        self.repository = repository
        super().__init__(f'Actor type must be defined in repository: {repository}')


class ActorException(Exception):
    def __init__(
        self,
        code: int,
        message: str,
        details: collections.abc.Sequence | collections.abc.Mapping | None = None
    ):
        self.code = code
        self.message = message
        self.details = details
