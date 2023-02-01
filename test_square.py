"""test_square test the module sqaure capabilities
        Module sqaure testing methods
    """
import unittest
import square


class TestSquare(unittest.TestCase):
    """TestSquare

    Args:
        unittest : Test the square module capabilitites
    """

    def test_square(self):
        """test_square
            Unit testing the method square
        """
        self.assertEqual(square.square(2), 4)
        self.assertEqual(square.square(3), 9)


if __name__ == '__main__':
    unittest.main()
