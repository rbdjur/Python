'''
import unitttest and the file test1
'''
import unittest
import test1

'''
create a class that inherits unittest and the class TesetCase
'''
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = test1.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = test1.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == "__main__":
    unittest.main()


