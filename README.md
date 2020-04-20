# ESP8266MicroPythonClock
Clock implemented using ESP8266 MCU and MicroPython

Credits: 
* LCD I2C driver is from https://github.com/dhylands/python_lcd/tree/master/lcd
* Wiring see https://dronebotworkshop.com/lcd-displays-arduino/

Setup:
1. Use pipenv https://pipenv.readthedocs.io/en/latest/ to hydrate your environment.
```bash
    pipenv shell
```
2. Connect your NodeMCPU to your wifi network. 
```Python
import network                                                                                                                                                                                                                                
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)                                                                                                                                                                                    
sta_if.scan()                             # Scan for available access points                                                                                                                                                                  
sta_if.connect("<AP_name>", "<password>") # Connect to an AP                                                                                                                                                                                  
sta_if.isconnected()                      # Check for successful connection    
```
 3. Run rshell and copy esp8266_i2c_lcd.py, lcd_api.py, main_2004_i2c_LCD_test.py, main_1602_i2c_LCD.py files to ESP8266
 NodeMCU (with MicroPython firmware), rename either of the main_xxx.py file as main.py, and reboot the MCU. 
 main_1602_i2c_LCD.py --- Clock. 
 main_2004_i2c_LCD_test.py --- test 2004 LCD. No clock function. 