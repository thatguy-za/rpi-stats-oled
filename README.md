# rpi-stats-oled

A basic script to display a raspberry pi's hostname and IP address on a oled display.

**Install guide**
1. Install the Adafruit SSD1306 library for the oled display
`sudo pip3 install adafruit-circuitpython-ssd1306`
2. Install Python Imaging Library so you can send text and images to the oled display
`sudo apt-get install python3-pil`
3. Copy the screen.py file onto the pi
4. Test that everything works by running `python screen.py`
5. Update your crontab by running `crontab -e` and adding a line to it to run the screen.py script however frequently you want it to be run.


I had some trouble getting this to work on OpenMediaVault ontop of Raspberry Pi OS lite 64bit and had to install the following packages
`sudo apt install python3-dev python3-setuptools`
