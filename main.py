# This project is create by Arbaz Memon Student of Electronics And Communication



from machine import Pin, I2C
import dht
import ssd1306
import time

# ESP32 Pin assignment

dht_sensor=dht.DHT22(Pin(14))
led=Pin(13,Pin.OUT)

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# make function to measure temperature and humidity value from dht sensor

def read_sensor():
    dht_sensor.measure()
    temp=dht_sensor.temperature()
    hum=dht_sensor.humidity()

    return temp,hum

# make function that take temperature and humidity value and diplay tham

def oled_display(temp,hum):
    oled.fill(0) # clear display
    oled.text('Temperature ', 0 ,0)  #(text , 0 pixel from left,0 pixel from top)
    oled.text("{:.1f} c ".format(temp),0,15) # {:.1f} us to formet temp value and convert into it string
    oled.text('Humidity', 0,30)
    oled.text('{:.1f}%'.format(hum),0,45)
    oled.show()

while True:
    try:
        temperature,humidity=read_sensor()
        oled_display(temperature,humidity)
        led.value(1)
        time.sleep(1)
        time.sleep(5)

        
    except OSError as e:
        print('Failed to read sensor.')
