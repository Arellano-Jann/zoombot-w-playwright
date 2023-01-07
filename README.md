# zoombot-w-playwright
https://playwright.dev/python/docs/intro

## To add
1. ~~Time in meeting~~
2. Popup handling. Unsure if it ACTUALLY does it or just says it does. Screenshot in headless to debug.
3. Handling polls
4. Checking sound (maybe by network) to see if there's people talking
5. Creating a log of the text chat
6. Creating a log of the transcription
7. I wonder if you can record in headless. I don't think so though. Counter to this is to take a screenshot every few seconds and play those images in sequential order. Put it into a folder of course.x
8. Access transcription/log and if name has been said, issue a wakeup call or playa prerecorded "idk"


Ubuntu Setup
```bash
sudo apt update
sudo apt install python3-pip
pip install pytest-playwright
# export PATH="/home/<name>/.local/bin:$PATH"
export PATH="/home/jannarellano/.local/bin:$PATH"
source ~/.bash_profile
playwright install
playwright install-deps
```

Running the app
```bash
# Run app
python3 zoombot2.py
```

Running playwright codegen
```bash
# playwright codegen <site>
playwright codegen https://unr.zoom.us/j/83958869209?uname=Jann+Arellano
```

WSL2 can run GUI apps natively now according to this https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps
as long as it's Windows 11 or a high version of Windows 10 + Windows Insider (and updated drivers)