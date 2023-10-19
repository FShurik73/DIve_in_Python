from task_1 import clear_text
import unittest

class TestUnitMy(unittest.TestCase):
    
    def setUp(self) -> None:
        self.correct = 'text'
        self.first = 'TexT'
        self.second = 'te..xT'
        self.third = 'TeЯ..xT'
        self.forth = 'TeююЯЯ..xT'

    def test1(self):
        self.assertEqual(self.correct, clear_text(self.first))

    def test2(self):
        self.assertTrue(self.correct == clear_text(self.correct))

    def test3(self):
        self.assertFalse(self.correct is clear_text(self.third))

    def test4(self):
        self.assertRaises(ValueError, clear_text, None)

if __name__ == '__main__':
    unittest.main(verbosity=2)