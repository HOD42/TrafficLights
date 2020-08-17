from time import sleep
import RTk.GPIO
pause=2
gpios=[2,3,4]
RTk.GPIO.setmode(RTk.GPIO.BCM)
for pin in gpios:
    print("Activate pin ", pin)
    RTk.GPIO.setup(pin,RTk.GPIO.OUT)
    RTk.GPIO.output(pin,1)
    sleep(pause)
    RTk.GPIO.output(pin,0)
print("All done!")
