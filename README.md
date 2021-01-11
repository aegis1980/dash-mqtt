# Dash with MQTT

`dash_mqtt` is a Dash component library for adding MQTT messaging functionality to your Dash apps.
It is essentially a wrapper around [MQTT.js](https://github.com/mqttjs/MQTT.js).

## Usage

Simple echo example using [emqx.io](https://www.emqx.io/) test MQTT broker. 

```

import dash_mqtt
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc

TEST_SERVER = 'broker.emqx.io'
TEST_SERVER_PORT = 8083
TEST_SERVER_PATH = 'mqtt'
MESSAGE_OUT_TOPIC = 'testtopic'
MESSAGE_IN_TOPIC = 'testtopic'

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_mqtt.DashMqtt(
        id='mqtt',
        broker_url=TEST_SERVER,
        broker_port = TEST_SERVER_PORT,
        broker_path = TEST_SERVER_PATH,
        topics=[MESSAGE_IN_TOPIC]
    ),
    html.H1('MQTT echo'),
    html.P('MQTT echo server to ' + TEST_SERVER + ' on port ' + str(TEST_SERVER_PORT)),
    dcc.Input(
        id='message_to_send',
        placeholder='message to send',
        debounce = True),
    html.Button('Send',id='send'),
    html.Div(id='return_message')
])


@app.callback(
        Output('mqtt', 'message'),
        Input('send', 'n_clicks'),
        State('message_to_send', 'value')
    )
def display_output(n_clicks, message_payload):
    if n_clicks:
        return {
            'topic': MESSAGE_OUT_TOPIC,
            'payload' : message_payload
        }
    return dash.no_update
```

### NOTE

MQTT.js is running as an MQTT client in the browser in this implementation (As a React component as per typical Dash components). Subsequently, from [here](https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483):
1. There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
2. To get around this limitation, **MQTT.js** uses **MQTT over WebSockets** instead when it detects it's running in a browser.

This means that you need to set the `broker_port` up to point at the MQTT-over-WebSockets port of the MQTT broker you are using, or if you are setting up your own broker server, turn on **MQTT-over-WebSockets** and expose a port.

---
## Help with developing the component

If you are want to adapt or help develop the component, refer [README_DEV.md](./README_DEV.md)

Currently written to suit author's needs - MQTT broker running in a DOcker Container on a local network for home IOT scenarion using [IOTStack](https://sensorsiot.github.io/IOTstack/), so have not put any effort into encrypted messaging. 