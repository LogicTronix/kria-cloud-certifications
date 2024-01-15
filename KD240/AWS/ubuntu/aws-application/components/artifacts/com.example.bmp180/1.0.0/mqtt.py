import time
import traceback
import json
import gpiod
from bmp180 import bmp180

bmp = bmp180(0x77)

LED_PIN = 2
BUTTON_PIN = 1

import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS,
    PublishToIoTCoreRequest,
    SubscribeToIoTCoreRequest
)

publishbmp = "kd240/bmp180"
subscribetopic = "kd240/mqtt"
message =  {
  "button": "button pressed",
  "timemillis": 000000000000
}

bmp_data = {
        "temperature" : "0.00",     
        "timemillis": 0000000000000
}

TIMEOUT = 10
qos = QOS.AT_LEAST_ONCE
subqos = QOS.AT_MOST_ONCE

ipc_client = awsiot.greengrasscoreipc.connect()


def bmp180publish(channel):
    print('publishing temperature from bmp180')

    bmp_data["timemillis"] = round(time.time() * 1000)
    bmp_data["temperature"] = str(bmp.get_temp())
    msgstring = json.dumps(bmp_data)

    pubrequest = PublishToIoTCoreRequest()
    pubrequest.topic_name = publishbmp
    pubrequest.payload = bytes(msgstring, "utf-8")
    pubrequest.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(pubrequest)
    future = operation.get_response()
    future.result(TIMEOUT)


# Keep the main thread alive, or the process will exit.
try:
    while True:
        bmp180publish(4)
        time.sleep(10)
        pass
        
finally:
    print("button event detect finished")
