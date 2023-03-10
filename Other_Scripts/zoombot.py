# Basic Join Meeting Script

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://unr.zoom.us/j/83958869209?uname=Jann+Arellano")
    page.goto("https://tmcc-edu.zoom.us/j/5867770981#success") # Link
    
    page.get_by_role("button", name="Join from Your Browser").click() # Joins from browser
    page.wait_for_load_state() # Waits to avoid problem
    page.get_by_placeholder("Your Name").fill("Jann Arellano") # Fill in name
    page.get_by_role("button", name="Join").click() # Join session
    
    page.wait_for_timeout(310000) # Time in meeting (in milliseconds)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
