import households
import unittest
# unittest documentation: https://docs.python.org/3/library/unittest.html

'''
The structure of test:

    Create your inputs
    Execute the code being tested, capturing the output
    Compare the output with an expected result

https://realpython.com/python-testing/
'''

class FOCtest(unittest.TestCase):
    def test_FOCs():
        b_sp1 = (1, 2, 3)
        n_s = (1.0, 1.0, 0.2)
        0.9, 1, 0.2, 1, 0.5, 0.5, 0.1, 0 = args
        #    beta, sigma, r, w, b_init, l_tilde, chi, theta = args

        foc_errors = households.FOCs(b_sp1, n_s, *args)

        assert()

if __name__ == '__main__':
    unittest.main()
