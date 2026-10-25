import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = sorted((ROOT / "scripts").glob("*.py"))


def test_scripts_exist():
    assert SCRIPTS, "no scripts found in scripts/"


@pytest.mark.parametrize("script", SCRIPTS, ids=lambda p: p.name)
def test_script_compiles(script):
    compile(script.read_text(), str(script), "exec")


EXPECTED_FUNCTIONS = [
    ("01_prepare_data", "prepare_data"),
    ("02_exploratory_data_analysis", "run_eda"),
    ("03_differential_expression", "run_deseq"),
    ("04_pathway_analysis", "run_gsea"),
]


@pytest.mark.parametrize("script, func", EXPECTED_FUNCTIONS)
def test_function_exists(load_script, script, func):
    module = load_script(script)
    assert callable(getattr(module, func, None)), f"{script}.py is missing {func}()"


def test_download_script_syntax():
    subprocess.run(["bash", "-n", str(ROOT / "download_dataset.sh")], check=True)
