import threading
import grovepi 
from raspberry_pi.Raspberry_SDK.Countly import Countly
 
light_sensor = 0
 
countly = Countly("SERVER_URL", "APP_KEY", 0)
 
def grove():
      threading.Timer(30,grove).start()
       countly.event("Light", int(grovepi.analogRead(light_sensor)/10.24))
 
grove()
#Example for a light sensor controlled through raspberry pi and a representative of python's use in iot