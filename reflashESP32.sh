#!/bin/bash
# curl -o .esp32firmware.bin https://micropython.org/resources/firmware/esp32-idf3-20200420-v1.12-387-g1b1ceb67b.bin
curl -o .esp32firmware.bin https://micropython.org/resources/firmware/esp32-idf3-20191220-v1.12.bin
esptool.py --port /dev/ttyUSB0 erase_flash && esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 .esp32firmware.bin && rshell -p /dev/ttyUSB0 --buffer-size=30
