# zoombot-w-playwright
https://playwright.dev/python/docs/intro

## To add
1. ~~Time in meeting~~
2. ~~Popup handling. Unsure if it ACTUALLY does it or just says it does. Screenshot in headless to debug.~~ I think it handles popups in headless judging from the screenshots
3. Handling polls
4. Checking sound (maybe by network) to see if there's people talking
5. Creating a log of the text chat
6. Creating a log of the transcription
7. I wonder if you can record in headless. I don't think so though. Counter to this is to take a screenshot every few seconds and play those images in sequential order. Put it into a folder of course.x
8. Access transcription/log and if name has been said, issue a wakeup call or playa prerecorded "idk"
9. Waiting room logic
10. Join Zoom Breakout room - do this by tuesday or tomorrow morning

## Known Issues
1. Link is wonky and has to be fully working/loaded beforehand. I put "#success" at the end of the zoom link to have it automatically loaded. I think it's a memory issue but I believe that the 2 root causes are: auto-downloading the app or a popup (not seen in the screenshots). I'm not really sure but I've tried: `on(download)`, `on(dialog)`, `wait_for_load_state()`, `slow_mo=10000`, `timeout=0` and there still is the horrific never ending loading.
2. ~~Unable to run on standard Amazon Linux EC2 instance right now. Potential fix is to use a docker image instead to bundle everthing up nicely.~~ Will not fix this as running docker on Linux EC2 is a piece of work when you can just spin up a Ubuntu instance.

## Setup

### Ubuntu Setup
```bash
sudo apt update
sudo apt install python3-pip
git clone https://github.com/Arellano-Jann/zoombot-w-playwright
pip install pytest-playwright
pip install schedule
# export PATH="/home/<name>/.local/bin:$PATH"
export PATH="/home/jannarellano/.local/bin:$PATH"
source ~/.bash_profile
playwright install
playwright install-deps
```

### EC2 Ubuntu Setup
```bash
sudo apt update
sudo apt install python3-pip -y
git clone https://github.com/Arellano-Jann/zoombot-w-playwright
pip install pytest-playwright
pip install schedule
# export PATH="/home/<name>/.local/bin:$PATH"
export PATH="/home/ubuntu/.local/bin:$PATH"
source ~/.bash_profile
playwright install
playwright install-deps
```

### ~~EC2 Amazon Linux Setup~~ Deprecated. Too much effort.
```bash
sudo yum -y install git
git clone https://github.com/Arellano-Jann/zoombot-w-playwright
pip3 install playwright
playwright install
# export PATH="/home/jannarellano/.local/bin:$PATH"
# source ~/.bash_profile
playwright install-deps
```

### Running the app
```bash
# Run app
cd zoombot-w-playwright
python3 zoombot2.py
# in ec2, constantly
nohup `python3 zoombot2.py` # add "&" to the end to get back the terminal
```

### Running playwright codegen
```bash
# playwright codegen <site>
playwright codegen https://unr.zoom.us/j/83958869209?uname=Jann+Arellano
```



## Other Notes
WSL2 can run GUI apps natively now according to this https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps
as long as it's Windows 11 or a high version of Windows 10 + Windows Insider (and updated drivers)