# Main Script

import config
from playwright.sync_api import Playwright, sync_playwright, expect

in_seconds = 1000 # aux variable to convert milli to seconds

# adds in audio controls
def run(playwright: Playwright) -> None:
    ### Joining
    
    # browser = playwright.chromium.launch(headless=False, slow_mo=5000)
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.screenshot(path="screenshots/11.png")
    print('Going to link:', config.meeting_link)
    page.goto(config.meeting_link) # Go to link
    print('Joined from browser and yeeting myself in...')
    page.screenshot(path="screenshots/12.png")
    page.get_by_role("button", name="Join from Your Browser").click() # Join from browser
    page.screenshot(path="screenshots/13.png")
    # page.locator('//a[@id="zoom-ui-frame"]/div[2]/div/div[2]/h3[2]/span/a') # ^ Join from browser xpath version
    
    print('Waiting for load state')
    page.wait_for_load_state()
    page.screenshot(path="screenshots/14.png")
    print('FYI: I put your name as:', config.nameTag)
    page.get_by_placeholder("Your Name").fill(config.nameTag) # Fill name
    
    # page.get_by_role("button", name="Join").click() # Join session
    page.locator('//button[@id="joinBtn"]').click() # ^ Join session by xpath
    print("Lol the join button was clicked... Hopefully we don't get caught playing hooky... Waiting for loading now")
    page.wait_for_load_state()
    
    ### Audio
    
    # page.get_by_role("button", name="More audio controls").click() # Bottom left more controls to leave audio
    # page.get_by_role("menuitem", name="Leave Computer Audio").click() # Leaves audio
    
    # might not need this lmao
    # page.get_by_role("tab", name="Computer Audio").locator("div").click() # Navigates to the Computer Audio tab
    # page.get_by_role("tab", name="Computer Audio").locator("div").click() # Navigates to the Computer Audio tab
    
    print("Joining audio...")
    # Div for audio wrapper
    # xpath = //*[@id="foot-bar"]/div[1]/div[1]
    # selector = #foot-bar > div:nth-child(1) > div:nth-child(1)
    page.screenshot(path="screenshots/1.png")
    # page.locator('//*[@id="voip-tab"]/div/button').click(timeout=0*in_seconds) # Joins audio through big blue button by xpath
    # page.get_by_role("button", name="Join Audio by Computer").click() # Joins audio
    ## Alt option
    ## page.get_by_role("tablist").get_by_role("button", name="close").press("Tab")
    ## page.get_by_role("button", name="Join Audio by Computer").press("Enter")
    print('Joined audio. I can now hear the screams of terror')
    page.screenshot(path="screenshots/2.png")
    page.wait_for_load_state() # Don't know why this is here but fuck it we ball
    
    # Not really sure what this tests for but i'll remove this later? I think it was just to see if the bottom left changed or if something pops up (which it does) or tests for the bug on the bottom which seemingly doesnt happen
    print('Testing audio thing')
    page.screenshot(path="screenshots/3.png")
    page.wait_for_timeout(10*in_seconds) 
    page.screenshot(path="screenshots/4.png")
    # might have a bug where browser has a popup asking for mic usage 
    # https://playwright.dev/python/docs/dialogs#alert-confirm-prompt-dialogs
    
    ### Meeting. Loop this with inside logic from 3-8
    
    # Time in meeting. Could use this module for logic in leaving the meeting early etc. For example: polls, creating a recording, checking sound.
    print(config.time_in_meeting*in_seconds, ' seconds until leaving the meeting')
    page.wait_for_timeout(config.time_in_meeting*in_seconds) # Time(out) until leaving the meeting executes
    page.screenshot(path="screenshots/5.png")
    
    ### Leave the meeting
    print("We just kool aid manned the doors and exited the meeting hehe!!!")
    page.get_by_role("button", name="Leave").click() # Leaves the meeting
    page.screenshot(path="screenshots/6.png")
    page.get_by_role("menuitem", name="Leave Meeting").click() # Confirms the leaving of the meeting
    page.screenshot(path="screenshots/7.png")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
