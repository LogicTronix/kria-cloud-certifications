import time
import traceback
import json
import gpiod

LED_PIN = 1
BUTTON_PIN = 0
from gpiod.line import Direction, Value
EventType = gpiod.EdgeEvent.Type

import awsiot.greengrasscoreipc
import awsiot.greengrasscoreipc.client as client
from awsiot.greengrasscoreipc.model import (
    IoTCoreMessage,
    QOS,
    PublishToIoTCoreRequest,
    SubscribeToIoTCoreRequest
)

request = gpiod.request_lines(
    "/dev/gpiochip3",
    consumer="switch-example",
    config={
        BUTTON_PIN: gpiod.LineSettings(
            direction=Direction.INPUT,
			edge_detection=gpiod.line.Edge.BOTH,
            event_clock=gpiod.line.Clock.REALTIME
        ),
        LED_PIN: gpiod.LineSettings(
            direction=Direction.OUTPUT, output_value=Value.ACTIVE
        )

    },
)


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
                request.set_value(LED_PIN, Value.ACTIVE)
                
            else:
                print("turn off")
                request.set_value(LED_PIN, Value.INACTIVE)
                

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
        for event in request.read_edge_events():
            print(event)
            print(event.event_type)
            if (event.event_type == EventType.RISING_EDGE):
                print("Rising Edge")
                button4pressed(4)
        
finally:
    # led_line.release()
    # button_line.release()
    print("Release Gpio")


print("button event detect finished")
