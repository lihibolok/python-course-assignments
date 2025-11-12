import os, sys
import math

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from nernst_logic import nernst_potential_mv


def test_positive_values():
    result = nernst_potential_mv(145, 12, 1, 37)
    assert math.isclose(result, 66.59, rel_tol=0.01)


def test_equal_concentrations():
    result = nernst_potential_mv(10, 10, 1, 37)
    assert math.isclose(result, 0.0, abs_tol=1e-3)
