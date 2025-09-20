from machine import Pin, PWM
import time
# MADE FOR MICROPYTHON DEVICES UPON BOOT
sp = PWM(Pin(7))
sp.freq(600)
sp.duty_u16(32768)
time.sleep(0.5)
sp.duty_u16(0)
time.sleep(3) # SAFE BOOT DELAY
# DO NOT MODIFY ANYTHING WITH DUTY_U16
