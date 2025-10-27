import importlib
import pkgutil

__all__ = []

def _import_modules():
    # Dynamically import all submodules inside this package
    for loader, moduleName, isPkg in pkgutil.iter_modules(__path__):
        if isPkg:
            continue  # skip any subpackages
        __all__.append(moduleName)
        module = importlib.import_module(f"{__name__}.{moduleName}")
        globals()[moduleName] = module

_import_modules()
