
import array

import dash_mqtt
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc


MESSAGE_OUT_TOPIC = 'test_out'
MESSAGE_IN_TOPIC = 'test_in'

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_mqtt.DashMqtt(
        id='mqtt',
        broker_url='192.168.1.30',
        topics=[MESSAGE_IN_TOPIC]
    ),
    dcc.Input(id='message_to_send', debounce = True),
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


@app.callback(
    Output('return_message', 'children'),
    Input('mqtt', 'incoming')
)
def display_incoming_message(incoming_message):
    if (incoming_message and incoming_message['payload'] and incoming_message['type'] == 'Buffer'):
        bytelist = incoming_message['payload']['data']
        return array.array('B', bytelist).tostring().decode('UTF-8')
    else:
        return dash.no_update


if __name__ == '__main__':
    app.run_server(debug=True)
