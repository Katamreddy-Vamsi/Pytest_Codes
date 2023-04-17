import sys
# sys.path.append(sys.path[0] + "/...")
import os

sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.test_LT_HomePage import test_LT_HomePage
from Test.Scripts.test_LT_LoginPage import test_LT_LoginPage

import testtools as testtools

if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(test_LT_HomePage),
        test_loader.loadTestsFromTestCase(test_LT_LoginPage),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
