from machine import Pin, PWM, SoftI2C
from ssd1306 import SSD1306_I2C
import time
# MADE FOR MICROPYTHON DEVICES UPON BOOT
o_w = 128
o_h = 64
i2c = SoftI2C(sda=Pin(14), scl=Pin(15))
oled = SSD1306_I2C(o_w. o_h, i2c)
sp = PWM(Pin(7))
oled.text("BOOT")
sp.freq(600)
sp.duty_u16(32768)
time.sleep(0.5)
sp.duty_u16(0)
oled.fill(0)
time.sleep(3) # SAFE BOOT DELAY
# DO NOT MODIFY ANYTHING WITH DUTY_U16 ABOVE
# LEAVE BELOW UNTOUCHED
#THIS SOFTWARE REQUIRES THE SSD1306 PACKAGE AND THE MICROPYTHON FIRMWARE

