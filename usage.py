
import dash_mqtt
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import time


TEST_SERVER = 'localhost'
TEST_SERVER_PORT = 1884
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
        topics=[MESSAGE_IN_TOPIC],
        message_processing_delay_ms=10,
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


# @app.callback(
#         Output('mqtt', 'message'),
#         Input('send', 'n_clicks'),
#         State('message_to_send', 'value')
#     )
# def display_output(n_clicks, message_payload):
#     if n_clicks and n_clicks>0:
#         return {
#             'topic': MESSAGE_OUT_TOPIC,
#             'payload' : message_payload
#         }
#     return dash.no_update


@app.callback(
    Output('mqtt', 'callback_complete'),
    Output('return_message', 'children'),
    Input('mqtt', 'incoming')
)
def display_incoming_message(incoming_message):
    if (incoming_message):
        print(f"Incoming message {incoming_message}")
        # time.sleep(1)
        return True, incoming_message['payload']
    else:
        return True, dash.no_update


if __name__ == '__main__':
    app.run(debug=True)

