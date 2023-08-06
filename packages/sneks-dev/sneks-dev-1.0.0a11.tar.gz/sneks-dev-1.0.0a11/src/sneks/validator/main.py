import pytest

path_to_test = "./submissions/better"


def main(test_path: str = None) -> int:
    if test_path is not None:
        global path_to_test
        path_to_test = test_path
    return pytest.main(["--pyargs", "sneks.validator"])
