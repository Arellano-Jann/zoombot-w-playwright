# Main Script

import config
from playwright.sync_api import Playwright, sync_playwright, expect

in_seconds = 1000 # aux variable to convert milli to seconds

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
    
    print("Joining audio...")
    page.locator('//*[@id="voip-tab"]/div/button').click(timeout=120*in_seconds) # Joins audio by xpath
    # page.get_by_role("button", name="Join Audio by Computer").click() # Joins audio
    print('Joined audio. I can now hear the screams of terror')
    page.wait_for_load_state() # Don't know why this is here but fuck it we ball
    
    print('Testing audio thing')
    page.wait_for_timeout(10*in_seconds) 
    # might have a bug where browser has a popup asking for mic usage 
    # https://playwright.dev/python/docs/dialogs#alert-confirm-prompt-dialogs
    
    # Time in meeting. Could use this module for logic in leaving the meeting early etc. For example: polls, creating a recording, checking sound.
    print(config.time_in_meeting*in_seconds, ' seconds until leaving the meeting')
    page.wait_for_timeout(config.time_in_meeting*in_seconds) # Time(out) until leaving the meeting executes
    
    print("We just kool aid manned the doors and exited the meeting hehe!!!")
    page.get_by_role("button", name="Leave").click() # Leaves the meeting
    page.get_by_role("menuitem", name="Leave Meeting").click() # Confirms the leaving of the meeting

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
