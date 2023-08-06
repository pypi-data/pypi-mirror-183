# Classes
class definded:
    @staticmethod
    def __getmembers(__obj, __type, __local_modules=...):...
    @staticmethod
    def modules(imported_script, local_modules) -> set:
        '''Returns a list of modules has been imported'''
    @staticmethod
    def objects(imported_script, local_modules) -> set:
        '''Returns a dictionary that maps the object's name to its class for each object in imported script'''

class CalledTimeCountable(object):
    def __init__(self, target): ...
    def __call__(self, *args, **kwargs): ...

# Functions
def stdOutput(target, *args, **kwargs) -> str: ...
def get_test_script_words(workdir=..., exceptions=...) -> dict:...

# Constant
DEFAULT_EXCEPTION_PATHS = ...