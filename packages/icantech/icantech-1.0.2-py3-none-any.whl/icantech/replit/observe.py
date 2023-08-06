import ast
import inspect
import sys
import io
import os

DEFAULT_EXCEPTION_PATHS = [
    '.cache', '.config', '.upm',
    'poetry.lock', '.breakpoints',
    'pyproject.toml', 'replit.nix', 
    '.replit', 'venv', '.lesson',
    '_test_runnertest_runner',
    '_test_runnertest_suite'
]

class definded:
    @staticmethod
    def __getmembers(__obj, __type, __local_modules):
        res = set()
        if __type == "module":
            modules = set()
            def visit_Import(node):
                for name in node.names:
                    modules.add(name.name.split('.')[0])
            def visit_ImportFrom(node):
                if node.module is not None and node.level == 0:
                    modules.add(node.module.split('.')[0])
            node_it = ast.NodeVisitor()
            node_it.visit_Import = visit_Import
            node_it.visit_ImportFrom = visit_ImportFrom
            with open(__obj.__file__, 'r', encoding='utf-8') as f:
                node_it.visit(ast.parse(f.read()))
            res = modules

        for name, obj in inspect.getmembers(__obj):
            if '__' in name: continue
            if f'<{__type}' in str(obj) or f'<built-in {__type}' in str(obj):
                res.add(name)
            if '<module' in str(obj):
                if (
                    name in __local_modules or
                    str(obj).split()[1][1:-1] in __local_modules
                ):
                    res |= definded.__getmembers(obj, __type, __local_modules)
        return res

    @staticmethod
    def modules(imported_module, local_modules):
        return definded.__getmembers(imported_module, 'module', local_modules)

    def objects(imported_module, local_modules):
        return (
            definded.__getmembers(imported_module, 'function', local_modules) |
            definded.__getmembers(imported_module, 'class', local_modules)
        )

class CalledTimeCountable(object):
    def __init__(self, target):
        self.target = target
        self.called_time = 0
    def __call__(self, *args, **kwargs):
        self.called_time += 1
        return self.target(*args, **kwargs)

def stdOutput(target, *args, **kwargs):
    stdout_backup = sys.stdout
    outstream = io.TextIOWrapper(io.BytesIO(), sys.stdout.encoding)
    sys.stdout = outstream
    target(*args, **kwargs)
    sys.stdout.seek(0)
    res = sys.stdout.read().strip()
    sys.stdout = stdout_backup
    outstream.close()
    return res

def get_test_script_words(workdir='.', exceptions=DEFAULT_EXCEPTION_PATHS):
    res = {}
    for name in os.listdir(workdir):
        if name in exceptions:  continue
        path = f'{workdir}/{name}'
        if os.path.isdir(path):
            res.update(get_test_script_words(path, exceptions))
            continue
        if name.endswith('.py'):
            with open(path, 'r', encoding='utf8') as f:
                key = path[2:-3].replace('/', '.')
                res[key] = f.read().split()
    return res