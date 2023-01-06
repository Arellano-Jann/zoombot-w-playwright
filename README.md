# zoombot-w-playwright
https://playwright.dev/python/docs/intro

Ubuntu Setup
```
sudo apt update
sudo apt install python3-pip
pip install pytest-playwright
# export PATH="/home/<name>/.local/bin:$PATH"
export PATH="/home/jannarellano/.local/bin:$PATH"
source ~/.bash_profile
playwright install
playwright install-deps
```

Running playwright codegen
```
# playwright codegen <site>
playwright codegen https://unr.zoom.us/j/83958869209?uname=Jann+Arellano
```