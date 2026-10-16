from pathlib import Path
import unittest

PROJECT_ROOT = Path(__file__).resolve().parent.parent


class ShoppingAppTests(unittest.TestCase):

    def test_homepage_exists(self):
        homepage = PROJECT_ROOT / "index.html"
        self.assertTrue(homepage.is_file())

    def test_homepage_has_title(self):
        homepage = PROJECT_ROOT / "index.html"
        content = homepage.read_text(encoding="utf-8")
        self.assertIn("Online Shopping Application", content)

    def test_stylesheet_exists(self):
        stylesheet = PROJECT_ROOT / "css" / "style.css"
        self.assertTrue(stylesheet.is_file())


if __name__ == "__main__":
    unittest.main()
