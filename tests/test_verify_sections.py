import pytest
import asyncio
from unittest.mock import MagicMock, AsyncMock, patch
from verify_sections import verify_sections

@pytest.mark.asyncio
async def test_verify_sections_success():
    # Mocking Playwright components
    mock_page = AsyncMock()
    mock_context = AsyncMock()
    mock_browser = AsyncMock()
    mock_playwright = AsyncMock()
    mock_p_manager = MagicMock()

    # Setup the mocks hierarchy
    mock_p_manager.__aenter__.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    # Setup page behaviors
    mock_page.goto.return_value = None
    mock_page.query_selector.return_value = MagicMock()
    mock_page.click.return_value = None
    mock_page.wait_for_timeout.return_value = None
    mock_page.is_visible.return_value = True
    mock_page.screenshot.return_value = None
    mock_page.inner_text.return_value = "Mocked H2 Content"

    with patch('verify_sections.async_playwright', return_value=mock_p_manager):
        results = await verify_sections(file_path="mock_path", screenshot_dir=None)

    assert len(results) == 6
    for section in results:
        assert results[section]['visible'] is True
        assert results[section]['h2'] == "Mocked H2 Content"
        assert results[section]['error'] is None

@pytest.mark.asyncio
async def test_verify_sections_missing_nav():
    mock_page = AsyncMock()
    mock_context = AsyncMock()
    mock_browser = AsyncMock()
    mock_playwright = AsyncMock()
    mock_p_manager = MagicMock()

    mock_p_manager.__aenter__.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    mock_page.goto.return_value = None
    # Mock query_selector to return None (nav link not found)
    mock_page.query_selector.return_value = None

    with patch('verify_sections.async_playwright', return_value=mock_p_manager):
        results = await verify_sections(file_path="mock_path", screenshot_dir=None)

    for section in results:
        assert results[section]['visible'] is False
        assert "Nav link" in results[section]['error']

@pytest.mark.asyncio
async def test_verify_sections_missing_h2():
    mock_page = AsyncMock()
    mock_context = AsyncMock()
    mock_browser = AsyncMock()
    mock_playwright = AsyncMock()
    mock_p_manager = MagicMock()

    mock_p_manager.__aenter__.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    mock_page.goto.return_value = None

    def query_selector_side_effect(selector):
        if "h2" in selector:
            return None # H2 not found
        return MagicMock() # Nav found

    mock_page.query_selector.side_effect = query_selector_side_effect
    mock_page.click.return_value = None
    mock_page.wait_for_timeout.return_value = None
    mock_page.is_visible.return_value = True
    mock_page.screenshot.return_value = None

    with patch('verify_sections.async_playwright', return_value=mock_p_manager):
        results = await verify_sections(file_path="mock_path", screenshot_dir=None)

    for section in results:
        assert results[section]['visible'] is True
        assert results[section]['error'] == "H2 not found"

@pytest.mark.asyncio
async def test_verify_sections_failure_handling():
    mock_page = AsyncMock()
    mock_context = AsyncMock()
    mock_browser = AsyncMock()
    mock_playwright = AsyncMock()
    mock_p_manager = MagicMock()

    mock_p_manager.__aenter__.return_value = mock_playwright
    mock_playwright.chromium.launch.return_value = mock_browser
    mock_browser.new_context.return_value = mock_context
    mock_context.new_page.return_value = mock_page

    mock_page.goto.return_value = None

    # Simulate a crash during click
    mock_page.query_selector.return_value = MagicMock()
    mock_page.click.side_effect = Exception("Page crashed")

    with patch('verify_sections.async_playwright', return_value=mock_p_manager):
        results = await verify_sections(file_path="mock_path", screenshot_dir=None)

    for section in results:
        assert results[section]['error'] == "Page crashed"
