import random  
import time  
from bmp180 import bmp180

bmp = bmp180(0x77)

  
from azure.iot.device import IoTHubDeviceClient, Message  
  
CONNECTION_STRING = "HostName=KR260-IoT-HUB.azure-devices.net;DeviceId=KD240-dev01;SharedAccessKey=+lVudFQBlUB2t3lfvlaRowOKzCDjLq5qDAIoTCsSR7Y="  
  
TEMPERATURE = 20.0  
HUMIDITY = 60  
MSG_TXT = '{{"temperature": {temperature},"pressure": {pressure}}}'  
  
def iothub_client_init():  
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
    return client  
  
def iothub_client_telemetry_sample_run():  
  
    try:  
        client = iothub_client_init()  
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )  
        while True:  
            
            temperature = TEMPERATURE + (random.random() * 15)  
            humidity = HUMIDITY + (random.random() * 20)  
            msg_txt_formatted = MSG_TXT.format(temperature=bmp.get_temp(), pressure=bmp.get_pressure())  
            message = Message(msg_txt_formatted)  
  
            if temperature > 30:  
              message.custom_properties["temperatureAlert"] = "true"  
            else:  
              message.custom_properties["temperatureAlert"] = "false"  
  
            print( "Sending message: {}".format(message) )  
            client.send_message(message)  
            print ( "Message successfully sent" )  
            time.sleep(3)  
  
    except KeyboardInterrupt:  
        print ( "IoTHubClient sample stopped" )  
  
if __name__ == '__main__':  
    print ( "IoT Hub Quickstart #1 - Simulated device" )  
    print ( "Press Ctrl-C to exit" )  
    iothub_client_telemetry_sample_run() 
