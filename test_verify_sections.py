import unittest
from unittest.mock import AsyncMock, patch, MagicMock
import asyncio
import os
from verify_sections import verify_sections

class TestVerifySections(unittest.IsolatedAsyncioTestCase):

    @patch('verify_sections.async_playwright')
    @patch('verify_sections.os.makedirs')
    async def test_verify_sections_happy_path(self, mock_makedirs, mock_async_playwright):
        # Setup mocks
        mock_playwright = AsyncMock()
        mock_async_playwright.return_value.__aenter__.return_value = mock_playwright

        mock_browser = AsyncMock()
        mock_playwright.chromium.launch.return_value = mock_browser

        mock_context = AsyncMock()
        mock_browser.new_context.return_value = mock_context

        mock_page = AsyncMock()
        mock_context.new_page.return_value = mock_page

        # Mock page methods
        mock_page.goto = AsyncMock()
        mock_page.click = AsyncMock()
        mock_page.wait_for_timeout = AsyncMock()
        mock_page.is_visible = AsyncMock(return_value=True)
        mock_page.screenshot = AsyncMock()
        mock_page.inner_text = AsyncMock(return_value="Mocked H2 Content")
        mock_browser.close = AsyncMock()

        # Run the function
        results = await verify_sections(file_path="mock_path.html", screenshot_dir="mock_dir")

        # Assertions
        self.assertEqual(len(results), 6)
        sections = ['about', 'experience', 'projects', 'skills', 'publications', 'conferences']
        for section in sections:
            self.assertIn(section, results)
            self.assertTrue(results[section]['visible'])
            self.assertEqual(results[section]['h2'], "Mocked H2 Content")
            self.assertEqual(results[section]['screenshot'], f"mock_dir/{section}.png")

        # Verify calls
        mock_page.goto.assert_called_once_with("mock_path.html")
        self.assertEqual(mock_page.click.call_count, 6)
        self.assertEqual(mock_page.is_visible.call_count, 6)
        self.assertEqual(mock_page.screenshot.call_count, 6)
        self.assertEqual(mock_page.inner_text.call_count, 6)
        mock_browser.close.assert_called_once()
        mock_makedirs.assert_called_with("mock_dir", exist_ok=True)

if __name__ == '__main__':
    unittest.main()
