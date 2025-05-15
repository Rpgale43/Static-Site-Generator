from textnode import *
from htmlnode import *

def main():
    TextNode1 = TextNode("This is some anchor text", TextType.LINK_TEXT, "https://www.boot.dev")
    HTMLNode1 = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
    LeafNode1 = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
    node = ParentNode("p", 
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )


    print(TextNode1)
    print(HTMLNode1)
    print(LeafNode1.to_html())
    print(node.to_html())


main()


