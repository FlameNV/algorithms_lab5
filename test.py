import unittest

from find_by_boyer_moore import FindByBoyerMoore


class Test(unittest.TestCase):

    def test(self):
        input_string = FindByBoyerMoore("Merry Christmas and Happy New Year!")
        self.assertEqual(input_string.search("Christmas"), [6])
        self.assertEqual(input_string.search("Year"), [30])

        input_string = FindByBoyerMoore("How long can this last please help me")
        self.assertEqual(input_string.search("help"), [30])
        self.assertEqual(input_string.search("long"), [4])


if __name__ == '__main__':
    unittest.main()
