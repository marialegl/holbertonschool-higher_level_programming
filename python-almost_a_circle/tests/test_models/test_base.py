import unittest

Base = __import__('base').Base

class Test_base(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def setUp(self):
        self.base = base()
    
    def test_string_reverse(self):
        self.assertEqual(self.StringManipulator.string_reverse('hola'), 'aloh')
        self.assertEqual(self.StringManipulator.string_reverse('mundo'), 'odnum')
        self.assertEqual(self.StringManipulator.string_reverse('holberton'), 'notrebloh')

    def test_string_reverse_number(self):
        with self.assertRaises(TypeError):
            self.StringManipulator.string_reverse(5)