import asyncio
from playwright.async_api import async_playwright
import os

async def verify_sections(file_path=None, screenshot_dir="verification/sections"):
    results = {}
    if file_path is None:
        file_path = "file://" + os.path.abspath("index.html")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1280, 'height': 800})
        page = await context.new_page()

        try:
            await page.goto(file_path)

            sections = ['about', 'experience', 'projects', 'skills', 'publications', 'conferences']

            if screenshot_dir:
                os.makedirs(screenshot_dir, exist_ok=True)

            for section in sections:
                section_result = {"visible": False, "h2": None, "error": None}
                try:
                    # Click the nav link
                    nav_selector = f"a[data-target='{section}']"
                    nav_element = await page.query_selector(nav_selector)
                    if nav_element:
                        await page.click(nav_selector)
                        # Wait for animation
                        await page.wait_for_timeout(500)

                        # Check if section is visible
                        is_visible = await page.is_visible(f"section#{section}")
                        section_result["visible"] = is_visible

                        if is_visible:
                            # Take screenshot
                            if screenshot_dir:
                                await page.screenshot(path=os.path.join(screenshot_dir, f"{section}.png"))

                            # Verify content is not empty (check for h2)
                            h2_selector = f"section#{section} h2"
                            h2_element = await page.query_selector(h2_selector)
                            if h2_element:
                                h2_content = await page.inner_text(h2_selector)
                                section_result["h2"] = h2_content
                            else:
                                section_result["error"] = "H2 not found"
                        else:
                            section_result["error"] = "Section not visible"
                    else:
                        section_result["error"] = f"Nav link for {section} not found"
                except Exception as e:
                    section_result["error"] = str(e)

                results[section] = section_result
                print(f"Section {section}: {section_result}")

        finally:
            await browser.close()

    return results

if __name__ == "__main__":
    asyncio.run(verify_sections())
