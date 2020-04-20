"""Implements a HD44780 character LCD connected via PCF8574AT on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms
from machine import I2C, Pin, Timer
from esp8266_i2c_lcd import I2cLcd

# PCF8574AT (comes with 1602 I2C LCD) default address: 0x3F
# PCF8574AT (comes with 2004 I2C LCD) default address is 0x27
DEFAULT_I2C_ADDR = 0x27

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 4, 20)

    lcd.clear()
    lcd.putstr("1234567890123456789\n2234567890123456789\n3234567890123456789\n4234567890123456789")
    sleep_ms(1000)
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr("12345678901234567890")
    lcd.move_to(0, 1)
    lcd.putstr("22345678901234567890")
    lcd.move_to(0, 2)
    lcd.putstr("32345678901234567890")
    lcd.move_to(0, 3)
    lcd.putstr("42345678901234567890")

#if __name__ == "__main__":
test_main()
