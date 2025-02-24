import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("p", "text inside",)
        self.assertEqual(node.tag, "p",)
        self.assertEqual(node.value, "text inside",)
        self.assertEqual(node.children, None,)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        node = HTMLNode("p", "text inside", None, {"href": "https://text.com"},)
        self.assertEqual(node.props_to_html(), ' href="https://text.com"',)

    def test_repr(self):
        node = HTMLNode("p", "text inside", None, {"href": "https://text.com"},)
        self.assertEqual(node.__repr__(),"HTMLNode(p, text inside, children: None, {'href': 'https://text.com'})")

    def test_to_html_no_children(self):
        node = LeafNode("p", "text inside")
        self.assertEqual(node.to_html(), "<p>text inside</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "text inside")
        self.assertEqual(node.to_html(), "text inside")

    def test_html_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_html_grandchildren(self):
        gchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [gchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text")
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()