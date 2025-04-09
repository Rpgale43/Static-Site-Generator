import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node3 = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev/")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)


if __name__ == "__main__":
    unittest.main()