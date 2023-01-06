from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, )
    context = browser.new_context()
    page = context.new_page()
    # page.goto("https://unr.zoom.us/j/83958869209?uname=Jann+Arellano")
    page.goto("https://tmcc-edu.zoom.us/j/5867770981")
    
    page.get_by_role("button", name="Join from Your Browser").click()
    page.get_by_placeholder("Your Name").fill("Jann Arellano")
    page.locator("#input-group").click()
    page.locator("#input-group").click()
    page.get_by_placeholder("Your Name").click()
    page.get_by_role("button", name="Join").click()
    frame.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
