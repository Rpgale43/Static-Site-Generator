import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test case 1: Node with props
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
        
        # Test case 2: Node without props
        node2 = HTMLNode("p", "hello from the paragraph")
        self.assertEqual(node2.props_to_html(), "")
        
        # Test case 3: Maybe another interesting case?
        # For example, a node with a single prop
        node3 = HTMLNode("div", props={"class": "container"})
        self.assertEqual(node3.props_to_html(), ' class="container"')

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode(value="Hello, world!")
        self.assertEqual(node2.to_html(), "Hello, world!")

        node3 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node3.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")



if __name__ == "__main__":
    unittest.main()