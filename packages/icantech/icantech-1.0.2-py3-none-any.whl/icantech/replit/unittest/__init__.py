import multiprocessing
import abc
import re
from ..observe import CalledTimeCountable

def _is_completed_in_limited_time(seconds, func, *args):
    test_thrd = multiprocessing.Process(target=func, args=args)
    test_thrd.start()
    test_thrd.join(seconds)
    if test_thrd.is_alive():
        test_thrd.terminate()
        return False
    return True

class __BaseTestCase(abc.ABC):
    def __init__(self, tester, failure_message):
        self.tester = tester
        self.failure_message = failure_message
    @abc.abstractmethod
    def run(self):...
    
class __KeywordCheckTest(__BaseTestCase):
    def __init__(self, tester, failure_message, test_script_words, workdir='.', exceptions=[]):
        self.test_script_words = test_script_words
        super().__init__(tester, failure_message)
    @abc.abstractmethod
    def run(self):...

class RequiredModuleTest(__BaseTestCase):
    def __init__(self, tester, failure_message, module_name, definded_modules):
        self.module_name = module_name
        self.definded_modules = definded_modules
        super().__init__(tester, failure_message)

    def run(self):
        __test_result = self.module_name in self.definded_modules
        self.tester.assertTrue(__test_result, self.failure_message)

class RequiredObjectTest(__BaseTestCase):
    def __init__(self, tester, failure_message, object_name, definded_objects):
        self.module_name = object_name
        self.definded_objects = definded_objects
        super().__init__(tester, failure_message)

    def run(self):
        __test_result = self.module_name in self.definded_objects
        self.tester.assertTrue(__test_result, self.failure_message)

class InvalidObjectTest(__KeywordCheckTest):
    def __init__(self, tester, failure_message, test_script_words, object_name, workdir='.', exceptions=[]):
        self.object_name = object_name
        super().__init__(tester, failure_message, test_script_words, workdir, exceptions)

    def run(self):
        for script in self.test_script_words:
            is_used = (
                # Direct usage
				re.search(f'\W+{self.object_name}\W+', ''.join(self.test_script_words[script])) is not None or
				# Indirect usage
                re.search(f'=\s*{self.object_name}[^\w+|.]', ''.join(self.test_script_words[script])) is not None
			)
            self.tester.assertFalse(is_used, self.failure_message)

class InvalidKeywordTest(__KeywordCheckTest):
    def __init__(self, tester, failure_message, test_script_words, keyword, workdir='.', exceptions=[]):
        self.keyword = keyword
        super().__init__(tester, failure_message, test_script_words, workdir, exceptions)

    def run(self):
        for script in self.test_script_words:
            is_used = self.keyword in self.test_script_words[script]
            self.tester.assertFalse(is_used, self.failure_message)

class InvalidOperatorTest(__KeywordCheckTest):
    def __init__(self, tester, failure_message, test_script_words, keyword, workdir='.', exceptions=[]):
        self.keyword = keyword
        super().__init__(tester, failure_message, test_script_words, workdir, exceptions)

    def run(self):
        for script in self.test_script_words:
            is_used = self.keyword in self.test_script_words[script]
            self.tester.assertFalse(is_used, self.failure_message)
            
class LimitTimeTest(__BaseTestCase):
    def __init__(self, tester, failure_message, time_limit, target):
        self.time_limit = time_limit
        self.target = target
        super().__init__(tester, failure_message)

    def run(self, *args, **kwargs):
        __test_result = _is_completed_in_limited_time(self.time_limit, self.target, *args, **kwargs)
        self.tester.assertTrue(__test_result, self.failure_message)

class RecursionTest(__BaseTestCase):
    def __init__(self, tester, failure_message, target, require_recursion=True):
        self.target = CalledTimeCountable(target)
        self.require_recursion = require_recursion
        super().__init__(tester, failure_message)

    def run(self, *args, **kwargs):
        self.target(*args, **kwargs)
        __test_result = self.require_recursion and self.target.called_time == 1
        self.tester.assertTrue(__test_result, self.failure_message)