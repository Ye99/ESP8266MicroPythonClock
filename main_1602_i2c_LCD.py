import ntptime
ntptime.settime()

"""Implements a HD44780 character LCD connected via PCF8574AT on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms, localtime
from machine import I2C, Pin, RTC, Timer
from esp8266_i2c_lcd import I2cLcd

# The PCF8574AT address: 0x3F
DEFAULT_I2C_ADDR = 0x3F

rtc = RTC()

motion = False

def handle_interrupt(pin):
  print("interrupt triggered")
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

def turn_off_relay():
  print("turn off relay")
  global motion
  motion = False
  relay.value(0)

# NodeMCU D5
relay = Pin(14, Pin.OUT)

# NodeMCU D6
pir = Pin(12, Pin.IN, Pin.PULL_UP)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

tim = Timer(-1)

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.putstr("It Works!\nSecond Line")
    sleep_ms(1000)
    lcd.clear()
    count = 0
    lcd.clear() # Don't call clear often as it causes screen flash. 
    while True:
        lcd.move_to(0, 0)
        t=localtime()
        # name = '{:04d}_{:02d}_{:02d}_{:02d}_{:02d}_{:02d}'.format(t[0], t[1], t[2], t[3], t[4], t[5])
        time = '{:04d}_{:02d}_{:02d}\n{:02d}_{:02d}_{:02d}'.format(t[0], t[1], t[2], t[3], t[4], t[5])
        lcd.putstr(time)
        sleep_ms(50)
        count += 1

        global motion
        if motion:
            print('Motion detected! Interrupt caused by:', interrupt_pin)
            relay.value(1)
            sleep_ms(500)
            motion = False
            relay.value(0)
            # tim.init(period=3000, mode=Timer.ONE_SHOT, callback=turn_off_relay)
            
#if __name__ == "__main__":
test_main()
