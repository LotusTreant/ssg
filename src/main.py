from textnode import TextNode, TextType

def main():
    input = TextNode("random text", TextType.ITALIC, "https://randomtext.com")
    print(input)

main()