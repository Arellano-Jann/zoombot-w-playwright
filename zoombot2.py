import config
from playwright.sync_api import Playwright, sync_playwright, expect

# adds in audio controls
def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    print('Going to link:', config.meeting_link)
    page.goto(config.meeting_link) # Go to link
    print('Joined from browser and yeeting myself in...')
    page.get_by_role("button", name="Join from Your Browser").click() # Join from browser
    
    print('Waiting for load state')
    page.wait_for_load_state()
    print('FYI: I put your name as:', config.nameTag)
    page.get_by_placeholder("Your Name").fill(config.nameTag) # Fill name
    
    # page.get_by_role("button", name="Join").click() # Join session
    page.locator('//button[@id="joinBtn"]').click() # ^ Join session by xpath
    print("Lol the join button was clicked... Hopefully we don't get caught playing hooky... Waiting for loading now")
    page.wait_for_load_state()
    
    # page.get_by_role("button", name="More audio controls").click() # Bottom left more controls to leave audio
    # page.get_by_role("menuitem", name="Leave Computer Audio").click() # Leaves audio
    
    # might not need this lmao
    # page.get_by_role("tab", name="Computer Audio").locator("div").click() # Navigates to the Computer Audio tab
    # page.get_by_role("tab", name="Computer Audio").locator("div").click() # Navigates to the Computer Audio tab
    
    print("Joined audio")
    page.locator('//*[@id="voip-tab"]/div/button').click(timeout=0) # Joins audio by xpath
    # page.get_by_role("button", name="Join Audio by Computer").click() # Joins audio
    
    print("We just kool aid manned the doors and exited the meeting hehe!!!")
    page.get_by_role("button", name="Leave").click() # Leaves the meeting
    page.get_by_role("menuitem", name="Leave Meeting").click() # Confirms the leaving of the meeting

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
