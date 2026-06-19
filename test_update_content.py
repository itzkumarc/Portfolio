import unittest
from update_content import update_html_content, PUBLICATIONS_NEW, CONFERENCES_NEW

class TestUpdateContent(unittest.TestCase):
    def test_update_publications_section(self):
        sample_content = """
        <html>
        <body>
            <!-- PUBLICATIONS SECTION -->
            <section id="publications" class="content-section">
                Old Publication Content
            </section>
            <!-- CONFERENCES SECTION -->
            <section id="conferences" class="content-section">
                Old Conference Content
            </section>
        </body>
        </html>
        """
        updated = update_html_content(sample_content)
        self.assertIn(PUBLICATIONS_NEW, updated)
        self.assertNotIn("Old Publication Content", updated)

    def test_update_conferences_section(self):
        sample_content = """
        <html>
        <body>
            <!-- PUBLICATIONS SECTION -->
            <section id="publications" class="content-section">
                Old Publication Content
            </section>
            <!-- CONFERENCES SECTION -->
            <section id="conferences" class="content-section">
                Old Conference Content
            </section>
        </body>
        </html>
        """
        updated = update_html_content(sample_content)
        self.assertIn(CONFERENCES_NEW, updated)
        self.assertNotIn("Old Conference Content", updated)

    def test_no_match(self):
        sample_content = "<html><body>No match here</body></html>"
        updated = update_html_content(sample_content)
        self.assertEqual(sample_content, updated)

if __name__ == '__main__':
    unittest.main()
