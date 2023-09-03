import pytest

@fixture
def simple_yaml():
    return """
    - 1
    - 2
    - 3
    """


def test_hard(simple_yaml):
    import dryaml  # noqa

    conf = dryaml.load(simple_yaml)
    assert conf == [1, 2, 3]
