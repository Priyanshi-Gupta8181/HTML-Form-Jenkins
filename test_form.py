
import unittest
from pathlib import Path
from html.parser import HTMLParser


class FormParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.forms = []
        self.inputs = []
        self.buttons = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.forms.append(attrs)

        elif tag == "input":
            self.inputs.append(attrs)

        elif tag == "button":
            self.buttons.append(attrs)


class TestHTMLForm(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        html_path = Path(__file__).parent / "index.html"

        parser = FormParser()

        with open(html_path, "r", encoding="utf-8") as file:
            parser.feed(file.read())

        cls.parser = parser

    def test_form_exists(self):
        self.assertGreater(
            len(self.parser.forms), 0,
            "HTML form not found"
        )

    def test_name_field_exists(self):
        self.assertTrue(any(
            field.get("id") == "name"
            and field.get("type") == "text"
            and "required" in field
            for field in self.parser.inputs
        ), "Required Name field not found")

    def test_email_field_exists(self):
        self.assertTrue(any(
            field.get("id") == "email"
            and field.get("type") == "email"
            and "required" in field
            for field in self.parser.inputs
        ), "Required Email field not found")

    def test_contact_field_exists(self):
        self.assertTrue(any(
            field.get("id") == "contact"
            and field.get("type") == "tel"
            and "required" in field
            for field in self.parser.inputs
        ), "Required Contact Number field not found")

    def test_submit_button_exists(self):
        self.assertTrue(any(
            button.get("type") == "submit"
            for button in self.parser.buttons
        ), "Submit button not found")


if __name__ == "__main__":
    unittest.main(verbosity=2)
