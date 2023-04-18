from unittest import TestLoader, TestSuite, TextTestRunner
from Pytest_Page_Object_Model.POM.Test.Scripts.test_Home_Page import Google_HomePage
from Pytest_Page_Object_Model.POM.Test.Scripts.test_Google_Search import Google_Search
import testtools
import sys
import os

# sys.path.append(sys.path[0] + "/...")
# print(sys.path[0])
# Uncomment if the above example gives you a relative path error


if __name__ == "__main__":
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(Google_HomePage),
        test_loader.loadTestsFromTestCase(Google_Search),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
    # self.driver.set_page_load_timeout(30))
