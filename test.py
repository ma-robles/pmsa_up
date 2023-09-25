from machine import Pin, I2C, RTC
from time import sleep_ms
from pmsa003 import PMSA_read


rtc = RTC()
i2c = I2C(0, scl=Pin(22, Pin.OPEN_DRAIN, Pin.PULL_UP),
          sda=Pin(21, Pin.OPEN_DRAIN, Pin.PULL_UP), freq=100000)
print(i2c.scan() )
n=0
list_data= [
    'PM1.0_ugm3',
    'PM2.5_ugm3',
    'PM10_ugm3',
    #'1.0um_0.1L',
    #'2.5um_0.1L',
    #'10um_0.1L',
    ]

while True:
    data = PMSA_read(i2c)
    date = rtc.datetime()
    date = date[0:3] + date[4:7]
    print(date, end=' ')
    #PM1, PM2.5, PM10
    for i,name in enumerate(list_data):
        print(data[name], end=' ')
    print()
    n+=1
    sleep_ms(60000)
