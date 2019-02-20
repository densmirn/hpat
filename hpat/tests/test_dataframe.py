import unittest
import pandas as pd
import numpy as np

import numba
import hpat
from hpat.tests.test_utils import (count_array_REPs, count_parfor_REPs,
    count_parfor_OneDs, count_array_OneDs, dist_IR_contains, get_start_end)


class TestDataFrame(unittest.TestCase):
    def test_create1(self):
        def test_impl(n):
            df = pd.DataFrame({'A': np.ones(n), 'B': np.random.ranf(n)})
            return df.A

        hpat_func = hpat.jit(test_impl)
        n = 11
        pd.testing.assert_series_equal(hpat_func(n), test_impl(n))

    def test_create_cond1(self):
        def test_impl(A, B, c):
            if c:
                df = pd.DataFrame({'A': A})
            else:
                df = pd.DataFrame({'A': B})
            return df.A

        hpat_func = hpat.jit(test_impl)
        n = 11
        A = np.ones(n)
        B = np.arange(n) + 1.0
        c = 0
        pd.testing.assert_series_equal(hpat_func(A, B, c), test_impl(A, B, c))
        c = 2
        pd.testing.assert_series_equal(hpat_func(A, B, c), test_impl(A, B, c))


if __name__ == "__main__":
    unittest.main()