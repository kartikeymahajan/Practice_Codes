from unittest import suite
from HTMLTestRunner import HTMLTestRunner
import unittest
from ut import Test

if __name__ == "__main__":
    # suite = unittest.makeSuite(Test)
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    filename = 'F:\Kartikeya\Git\Restaurant_Management_Unit_Testing\my_report.html'
    fp = open(filename, 'w')
    runner = HTMLTestRunner.HTMLTestRunner(fp,title=u'Unittest')
    runner.run(suite)