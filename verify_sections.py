import asyncio
from playwright.async_api import async_playwright
import os

async def verify_sections(file_path=None, screenshot_dir="verification/sections"):
    results = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        # Open the local index.html if file_path is not provided
        if file_path is None:
            file_path = "file://" + os.path.abspath("index.html")

        await page.goto(file_path)

        sections = ['about', 'experience', 'projects', 'skills', 'publications', 'conferences']

        if screenshot_dir:
            os.makedirs(screenshot_dir, exist_ok=True)

        for section in sections:
            print(f"Verifying section: {section}")
            # Click the nav link
            await page.click(f"a[data-target='{section}']")
            # Wait for animation
            await page.wait_for_timeout(500)

            # Check if section is visible
            is_visible = await page.is_visible(f"section#{section}")

            # Take screenshot if directory provided
            screenshot_path = None
            if screenshot_dir:
                screenshot_path = f"{screenshot_dir}/{section}.png"
                await page.screenshot(path=screenshot_path)

            # Verify content is not empty (check for h2)
            h2_content = await page.inner_text(f"section#{section} h2")

            results[section] = {
                "visible": is_visible,
                "h2": h2_content,
                "screenshot": screenshot_path
            }

            print(f"Section {section} visible: {is_visible}, H2: {h2_content}")

        await browser.close()
    return results

if __name__ == "__main__":
    asyncio.run(verify_sections())
