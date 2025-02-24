import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noeq(self):
        node = TextNode("This is not a text node", TextType.LINK, "https://texturl.com")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is not a url", TextType.NORMAL)
        node2 = TextNode("This is a URL", TextType.LINK, "https://texturl.com")
        self.assertIsNone(node.url)
        self.assertEqual(node2.url, "https://texturl.com")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://image.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props, {"src": "https://image.com", "alt": "This is an image"})

    def test_bold(self):
        node = TextNode("This is Bold text", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "This is Bold text")

if __name__ == "__main__":
    unittest.main()