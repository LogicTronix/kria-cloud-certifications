import time
import traceback
import json
import gpiod

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

chip = gpiod.Chip('gpiochip3')
led_line = chip.get_line(LED_PIN)
button_line = chip.get_line(BUTTON_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

publishtopic = "kr260/button"
subscribetopic = "kr260/mqtt"
message =  {
  "button": "button pressed",
  "timemillis": 000000000000
}

TIMEOUT = 10
qos = QOS.AT_LEAST_ONCE
subqos = QOS.AT_MOST_ONCE

ipc_client = awsiot.greengrasscoreipc.connect()

def button4pressed(channel):
    print('button pressed')

    message["timemillis"] = round(time.time() * 1000)

    msgstring = json.dumps(message)

    pubrequest = PublishToIoTCoreRequest()
    pubrequest.topic_name = publishtopic
    pubrequest.payload = bytes(msgstring, "utf-8")
    pubrequest.qos = qos
    operation = ipc_client.new_publish_to_iot_core()
    operation.activate(pubrequest)
    future = operation.get_response()
    future.result(TIMEOUT)


class SubHandler(client.SubscribeToIoTCoreStreamHandler):
    def __init__(self):
        super().__init__()

    def on_stream_event(self, event: IoTCoreMessage) -> None:
        try:
            message = str(event.message.payload, "utf-8")
            topic_name = event.message.topic_name
            # Handle message.
            jsonmsg = json.loads(message)

            if jsonmsg["ledon"]:
                print("true turn on")
                led_line.set_value(1)
                
            else:
                print("turn off")
                led_line.set_value(0)
                

        except:
            traceback.print_exc()

    def on_stream_error(self, error: Exception) -> bool:
        # Handle error.
        return True  # Return True to close stream, False to keep stream open.

    def on_stream_closed(self) -> None:
        # Handle close.
        pass




subrequest = SubscribeToIoTCoreRequest()
subrequest.topic_name = subscribetopic
subrequest.qos = subqos
handler = SubHandler()
operation = ipc_client.new_subscribe_to_iot_core(handler)
future = operation.activate(subrequest)
future.result(TIMEOUT)

# Keep the main thread alive, or the process will exit.
try:
    while True:
        button_state = button_line.get_value()
        if button_state == 0:
            button4pressed(4)
        else:
            print("button_released")
        
finally:
    led_line.release()
    button_line.release()


print("button event detect finished")
