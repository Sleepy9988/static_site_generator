import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_un_eq(self):
        node = HTMLNode("p", "Test-string")
        node2 = HTMLNode("a", "Another Test-string")
        self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        props_test = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode("p", "Test-string", props=props_test).props_to_html()
        toBe = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node, toBe)

    def test_to_html_props(self):
        node = HTMLNode(
                "div",
                "Hello, world!",
                None,
                {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
                node.props_to_html(),
                ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
                "div",
                "I wish I could read",
        )
        self.assertEqual(
                node.tag,
                "div",
        )
        self.assertEqual(
                node.value,
                "I wish I could read",
        )
        self.assertEqual(
                node.children,
                None,
        )
        self.assertEqual(
                node.props,
                None,
        )

    def test_repr(self):
        node = HTMLNode(
                "p",
                "What a strange world",
                None,
                {"class": "primary"},
        )
        self.assertEqual(
                node.__repr__(),
                "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main() 


