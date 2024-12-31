import os
import importlib

module_files = [
    f[:-3] for f in os.listdir(os.path.dirname(__file__))
    if f.endswith(".py") and f != "__init__.py"
]

for module_name in module_files:
    module = importlib.import_module(f".{module_name}", package=__name__)
    globals().update(
        {
            name: obj
            for name, obj in vars(module).items()
            if callable(obj)
        }
    )