# Just a list of the selectors I've been going through per codegen. Not for use as an actual bot.

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
    
    # Audio Testing
    page.locator("#multi-view-video").dblclick(position={"x":310,"y":101}) # Click on random position
    page.locator("#multi-view-video").click(position={"x":706,"y":83}) # Click on random Position
    page.get_by_text("Jann I ArellanoJann I Arellano").click() # Click on main tab name
    page.get_by_text("Jann I ArellanoJann I Arellano").click() # Click on main tab (not the name)
    page.get_by_role("button", name="audio").filter(has_text="Audio").click() # Bottom left click on audio (when not connected to audio/browser blocking audio)
    page.goto("https://tmcc-edu.zoom.us/wc/5867770981/join?track_id=&jmf_code=&meeting_result=&tk=&cap=undefined&refTK=&rn=false&epk=7ypBxoqjDQiZSfUf7pfTpwzQr9kHPNsnde_udFV8SJKzbU_HxyQ.l6XMzgjtc7WvKYwn") # refresh page (because I enabled browser audio by popup)
    page.get_by_role("button", name="mute my microphone").click() # Mute mic (connected to audio)
    page.get_by_role("button", name="unmute my microphone").click() # Unmute mic
    page.get_by_role("button", name="More audio controls").click() # Click on "^" icon for more options
    page.get_by_role("button", name="More audio controls").click() # Click again for some reason
    page.get_by_role("tablist").get_by_role("button", name="close").press("Tab") # Tab to join audio by computer. Probably a more reliable way to do this
    page.get_by_role("button", name="Join Audio by Computer").press("Enter") # Enter button to join
    
    # Polls
    page.locator("div").filter(has_text="Polls/Quizzes2 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").nth(2).click() # ]Click on box
    # 2 Choice Poll
    page.get_by_text("Polls/Quizzes2 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").click() # Click on Title header
    page.get_by_text("Polls/Quizzes2 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").click() # Click again for some reason
    page.get_by_role("radio", name="Choice 2").click() # Click on Choice 2
    page.get_by_role("radio", name="Choice 1").click() # //div[@id="0-0-0-1;1"]
    page.get_by_role("radio", name="Choice 1").click() # Click on Choice 1
    page.get_by_role("radio", name="Choice 2").click() # //div[@id="0-0-0-1;2"]
    page.get_by_role("radio", name="Choice 1").click() # Click again for more testing
    page.get_by_role("radio", name="Choice 1").click()
    page.get_by_role("button", name="Submit").click() # Click the submit button
    # 3 choice poll
    page.get_by_role("radio", name="Choice 1").click()
    page.get_by_role("radio", name="Choice 2").click()
    page.get_by_role("radio", name="Choice 3").click() # //div[@id="0-0-0-1;3"] 
    page.locator("#poll__body").click() # Click on body for some reason
    page.get_by_text("Polls/Quizzes3 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").press("Tab") # 1 tab through the program
    page.get_by_role("button", name="Close").press("Tab") # Tab again for some reason
    page.get_by_text("3 Question").press("Tab") # 2 tab through the program
    page.get_by_text("1. Untitled Question (Single Choice) *required").press("Tab") # 3 Tab through the question (thus going to Choice 1)
    page.get_by_role("radio", name="Choice 1").press("Enter") # pressed enter on choice 1
    page.get_by_role("radio", name="Choice 1").press("Tab") # so 4th tab to go to choice 2
    page.get_by_role("radio", name="Choice 2").press("Enter") # enter again
    page.get_by_role("radio", name="Choice 2").press("Tab") # 5 tab
    page.get_by_role("radio", name="Choice 3").press("Enter") 
    page.get_by_role("radio", name="Choice 3").press("Tab") # 6 tab
    page.get_by_text("1 of 1 answered").press("Tab") # tab through num of answered questions to go to submit button
    page.get_by_role("button", name="Submit").press("Enter") # enter on submit to finish poll
    # 4 Choice poll
    page.locator("div").filter(has_text="Polls/Quizzes4 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").nth(2).click()
    page.get_by_text("Polls/Quizzes4 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").press("Tab") # tabs again
    page.get_by_role("button", name="Close").press("Tab")
    page.get_by_text("4 Question").press("Tab")
    page.get_by_text("1. Untitled Question (Single Choice) *required").press("Tab")
    page.get_by_role("radio", name="Choice 1").press("Enter") 
    page.get_by_role("radio", name="Choice 1").press("Tab")
    page.get_by_role("radio", name="Choice 2").press("Enter")
    page.get_by_role("radio", name="Choice 2").press("Tab")
    page.get_by_role("radio", name="Choice 3").press("Enter")
    page.get_by_role("radio", name="Choice 3").press("Tab")
    page.get_by_role("radio", name="Choice 4").press("Enter")
    page.get_by_role("radio", name="Choice 4").press("Tab") # //div[@id="0-0-0-1;4"]
    page.get_by_text("1 of 1 answered").press("Tab")
    page.get_by_role("button", name="Submit").click() # click on submit # XPATH = //button[@id="polling-window"]/div[2]/div/div[4]/div[2]/button and SELECTOR = #polling-window > div.window-content > div > div.poll-footer > div.poll-footer__right > button 
    # Full 4 Choice Walk Through with tabs
    page.locator("#poll__body").click()
    page.get_by_text("Polls/Quizzes4 Question1. Untitled Question (Single Choice) *requiredChoice 1Cho").press("Tab") # X button
    page.get_by_role("button", name="Close").press("Tab") # 4 Question (Title of Poll)
    page.get_by_text("4 Question").press("Tab") # Question (Title of Question)
    page.get_by_text("1. Untitled Question (Single Choice) *required").press("Tab") # 1 Choice
    page.get_by_role("radio", name="Choice 1").press("Tab") # 2 Choice
    page.get_by_role("radio", name="Choice 2").press("Tab") # 3 Choice
    page.get_by_role("radio", name="Choice 3").press("Tab") # 4 Choice
    page.get_by_role("radio", name="Choice 4").press("Tab") # X Answered?
    page.get_by_text("1 of 1 answered").press("Tab") # Submit Button
    page.get_by_role("button", name="Submit").press("Tab") # Footer 1
    page.get_by_role("button", name="Who can see your responses?").press("Tab") # Footer 2

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
