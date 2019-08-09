# Seeed SGP30

The SGP30 is a digital multi-pixel gas sensor designed for easy integration into air purifier, demand-controlled ventilation, and IoT applications. Sensirion’s CMOSens®technology offers a complete sensor system on a single chip featuring a digital I2C interface, a temperature controlled micro hotplate, and two preprocessed indoor air quality signals. As the first metal-oxide gas sensor featuring multiple sensing elements on one chip, the SGP30 provides more detailed information about the air quality.


This code is for
- [Grove - VOC and eCO2 Gas Sensor (SGP30)](https://www.seeedstudio.com/Grove-VOC-and-eCO2-Gas-Sensor-SGP30-p-3071.html)

# Dependencies
This driver depends on:
- [***grove.py***](https://github.com/Seeed-Studio/grove.py)

This is easy to install with the following command.
 ```
curl -sL https://github.com/Seeed-Studio/grove.py/raw/master/install.sh | sudo bash -s -
 ```
## Installing from PyPI

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally from PyPI. To install for current user:
```
pip3 install seeed-python-sgp30
```
To install system-wide (this may be required in some cases):
```
sudo pip3 install seeed-python-sgp30
```


## Usage Notes

First, Check the corresponding i2c number of the board:
```
(.env) pi@raspberrypi:~ $ ls /dev/i2c*
/dev/i2c-1
```

Check if the i2c device works properly， 0x58 is the SGP30 i2c address.
```
pi@raspberrypi:~/Seeed_Python_SGP30 $ i2cdetect -y -r 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- 04 -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- 58 -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- -- 
```
Next, initialize the sersor object:
```python
import seeed_sgp30
from grove.i2c import Bus
sgp30 = seeed_sgp30.grove_sgp30(Bus(1)) #The default on the raspberry pie is 1, so you can also use Bus()
```
## Reading from the Sensor
To read from the sensor:
```python
data = sgp30.read_measurements()
co2_eq_ppm, tvoc_ppb = data.data
print("\r  tVOC = {} ppb CO2eq = {} ppm  ".format(
                             tvoc_ppb, co2_eq_ppm))
```

## Contributing
If you have any good suggestions or comments, you can send issues or PR us.
