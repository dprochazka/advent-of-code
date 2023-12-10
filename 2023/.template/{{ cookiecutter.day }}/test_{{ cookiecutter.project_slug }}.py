from {{ cookiecutter.project_slug }} import {{ cookiecutter.main_method }}

EXAMPLE = """
""".splitlines()

EXPECTED = None

def test_{{ cookiecutter.main_method }}():
    assert {{ cookiecutter.main_method }}(EXAMPLE) == EXPECTED
