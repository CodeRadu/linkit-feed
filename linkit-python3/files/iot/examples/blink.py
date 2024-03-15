import gpiod
import time

chipname = "gpiochip0" # The name of the gpio chip (gpiodetect)
linenumber = 14 # The line number (gpioinfo <gpiochip>)

chip = gpiod.Chip(chipname)
line = chip.get_line(linenumber)

line.request(consumer="my_gpio_control", type=gpiod.LINE_REQ_DIR_OUT) # Set the direction to OUTPUT

while True:
    line.set_value(1)
    time.sleep(0.5)
    line.set_value(0)
    time.sleep(0.5)

line.release()
chip.close()