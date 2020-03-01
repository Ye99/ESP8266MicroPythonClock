import ntptime
ntptime.settime()


"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms, localtime
from machine import I2C, Pin, RTC
from esp8266_i2c_lcd import I2cLcd

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x3F

rtc = RTC()

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

#if __name__ == "__main__":
test_main()
