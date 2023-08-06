from inspect import signature


class Predicate:
    def __init__(self, fn: callable):
        if not callable(fn):
            raise Exception('Expected a callable')
        self.fn = fn
        self.__args_count = len(signature(fn).parameters)
    
    def call(self, *args):
        return self.fn(*args[:self.__args_count])
