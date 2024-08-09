# Imports
import unittest
from hashtag_tool.hashtag_tool import filter_nonalum, convert

# Tester


class TestHashtagFunc(unittest.TestCase):

    def test_filter_nonalum(self):
        # Test that non-alphanumeric characters are removed
        self.assertEqual(filter_nonalum("Hello@World!"), "HelloWorld")
        self.assertEqual(filter_nonalum("123_ABC"), "123ABC")
        self.assertEqual(filter_nonalum(""), "")
        self.assertEqual(filter_nonalum("!@#$%^&*()"), "")

    def test_convert(self):
        # Test conversion to hashtags
        self.assertEqual(convert("Str1, St r2, sTR 3,"), "#str1 #str2 #str3 ")
        self.assertEqual(convert("Hello,World"), "#hello #world ")
        self.assertEqual(convert(""), "")
        self.assertEqual(convert(" , , "), "")
        self.assertEqual(convert("NoSpecialCharsAllowed!"),
                         "#nospecialcharsallowed ")
        self.assertEqual(convert("Multiple    Spaces"), "#multiplespaces ")
        self.assertEqual(convert("Mixed,Case"), "#mixed #case ")
        self.assertEqual(convert("Sometext, mixed with spaces, and new #$%#@!, CASEs"),
                         "#sometext #mixedwithspaces #andnew#$%#@! #CASEs ")


# Run PYTHONPATH=./src pytest
if __name__ == '__main__':
    unittest.main()
