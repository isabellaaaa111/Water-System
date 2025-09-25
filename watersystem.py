from gpiozero import OutputDevice
import datetime
import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def readData(channel):
    abc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((abc[1]&3) << 8) + abc[2]
    return data


needsWater = 630
pin_pump = 4 
pump = OutputDevice(pin_pump, active_high=True, initial_value=False)

raw_moisture = readData(0)
print(f"raw moisture: {raw_moisture}")

moisture_percentage = (raw_moisture / 1023.0) *100
f = open("/home/izzypi/WateringStats.txt", "a")
currentTime = datetime.datetime.now()
f.write(str(currentTime) + ":\n")
f.write("Current moisture: " + str(round(moisture_percentage,2)) + "% \n")

if moisture_percentage <60:
    pump.on()
    time.sleep(10)
    pump.off()
    f.write("Plants got watered!!!\n")

f.write("\n")
f.close




