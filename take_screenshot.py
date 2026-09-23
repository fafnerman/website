import sys
import os
from playwright.sync_api import sync_playwright

def take_screenshot(file_path, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        # Use file:// URL scheme
        url = "file:///" + file_path.replace("\\", "/")
        page.goto(url)
        page.wait_for_timeout(2000) # Wait for images to load if any
        page.screenshot(path=output_path, full_page=True)
        browser.close()

if __name__ == "__main__":
    take_screenshot(sys.argv[1], sys.argv[2])
