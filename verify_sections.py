import asyncio
from playwright.async_api import async_playwright
import os

async def verify_single_section(browser, section, file_path):
    context = await browser.new_context(viewport={'width': 1280, 'height': 800})
    page = await context.new_page()
    await page.goto(file_path)

    print(f"Verifying section: {section}")
    # Click the nav link
    await page.click(f"a[data-target='{section}']")
    # Wait for animation
    await page.wait_for_timeout(500)

    # Check if section is visible
    is_visible = await page.is_visible(f"section#{section}")
    print(f"Section {section} visible: {is_visible}")

    # Take screenshot
    await page.screenshot(path=f"verification/sections/{section}.png")

    # Verify content is not empty (check for h2)
    h2_content = await page.inner_text(f"section#{section} h2")
    print(f"Section {section} H2: {h2_content.strip()}")

    await context.close()

async def verify_sections():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Open the local index.html
        file_path = "file://" + os.path.abspath("index.html")
        sections = ['about', 'experience', 'projects', 'skills', 'publications', 'conferences']

        os.makedirs("verification/sections", exist_ok=True)

        # Run verifications concurrently
        tasks = [verify_single_section(browser, section, file_path) for section in sections]
        await asyncio.gather(*tasks)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_sections())
