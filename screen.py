import time
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

from datetime import datetime

i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

disp.fill(0)
disp.show()

width = disp.width
height = disp.height

padding = -2
top = padding
bottom = height - padding
x = 0
image = Image.new("1", (width, height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)

disp.contrast(10)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

cmd = "hostname -I | cut -d' ' -f1"
IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
cmd = "hostname"
hostname = subprocess.check_output(cmd, shell=True).decode("utf-8")

now = datetime.now()
timeNow = now.strftime("%H:%M %d/%m")

draw.text((x, top + 0), "Hostname: " + hostname, font=font, fill=255)
draw.text((x, top + 10), "IP: " + IP, font=font, fill=255)
draw.text((x, top + 20), "Updated: " + timeNow, font=font, fill=255)

# Display
disp.image(image)
disp.show()
