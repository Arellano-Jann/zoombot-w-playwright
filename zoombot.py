from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://unr.zoom.us/j/83958869209?uname=Jann+Arellano")
    page.goto("https://unr.zoom.us/j/83958869209?uname=Jann+Arellano#success")
    page.get_by_role("button", name="Join from Your Browser").click()
    page.get_by_placeholder("Your Name").click()
    page.get_by_placeholder("Your Name").fill("Jann Arellano")
    page.locator("#input-group").click()
    page.locator("#input-group").click()
    page.get_by_placeholder("Your Name").click()
    page.get_by_role("button", name="Join").click()
    page.goto("https://unr.zoom.us/wc/83958869209/join?track_id=&jmf_code=&meeting_result=&tk=&cap=undefined&refTK=&rn=false&po=7&epk=weKtDjKG9S22q5bx5QJkvNoOnnFdk88LwKBIXPL9cdX72Wf7U-0.Eq9Mlk2GpWP3LM_W")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
