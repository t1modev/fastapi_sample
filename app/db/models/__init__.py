import os
import glob
import inspect
from importlib import import_module

current_dir = os.path.dirname(__file__)

modules = glob.glob(os.path.join(current_dir, "*.py"))
module_names = [
    os.path.basename(f)[:-3]
    for f in modules
    if os.path.isfile(f) and not f.endswith("__init__.py")
]

for module_name in module_names:
    module = import_module(f".{module_name}", package=__name__)

    for name, obj in inspect.getmembers(module, inspect.isclass):
        if obj.__module__ == module.__name__:
            globals()[name] = obj