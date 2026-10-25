import importlib.util
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


def _load_script(name):
    """Import scripts/<name>.py as a module.

    Script names start with a digit (e.g. 01_prepare_data), which is not a
    valid identifier, so they cannot be imported with a normal import
    statement. Usage in a test:

        def test_prepare(load_script):
            prep = load_script("01_prepare_data")
            prep.prepare_data(...)
    """
    path = SCRIPTS_DIR / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def load_script():
    return _load_script
