from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://tmcc-edu.zoom.us/j/5867770981#success")
    page.get_by_role("button", name="Join from Your Browser").click()
    page.get_by_placeholder("Your Name").click()
    page.get_by_placeholder("Your Name").fill("Jann Arellano")
    page.get_by_role("button", name="Join").click()
    page.get_by_role("button", name="More audio controls").click()
    page.get_by_role("menuitem", name="Leave Computer Audio").click()
    page.get_by_role("tab", name="Computer Audio").locator("div").click()
    page.get_by_role("button", name="Join Audio by Computer").click()
    page.get_by_role("button", name="Leave").click()
    page.get_by_role("menuitem", name="Leave Meeting").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
