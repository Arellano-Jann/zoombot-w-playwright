import techwise
# import zoombot2
import schedule
import time

# Scheduler Runs on local PC time
# print("Fuck mondays. Garfield hates em.")
schedule.every().monday.at(config.hour).do(go)
schedule.every().tuesday.at(config.hour).do(go)
schedule.every().wednesday.at(config.hour).do(go)
schedule.every().thursday.at(config.hour).do(go)
# print("Yea wednesdays suck titties too... Slowest trading day of the week ong")
schedule.every().friday.at(config.hour).do(go)
# schedule.every().saturday.at(config.hour).do(go)
# print("LAST FUCKING TRADING DAY LETS GOOOOOO!!! THE STONKS ONLY GO ^^^^^^^^^^")

while True:
    schedule.run_pending()
    time.sleep(1)