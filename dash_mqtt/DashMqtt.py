# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashMqtt(Component):
    """A DashMqtt component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- state (dict; default {
    connected : false, 
    reconnecting : false
}): This MQTT connection state (in the readyState prop) and any associated information.
- broker_url (string; optional): The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org').
- protocol (string; optional): One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'.
Defaults to 'mqtt' which then is defaulted to 'ws' by MQTT.js 
From (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
To get around this limitation, MQTT.js uses MQTT over WebSockets instead when it detects it's running in a browser.
- broker_port (number; optional): The MQTT broker port, defaults to 
Default to 8080 as MQTT over WebSockets, unencrypted as per
https://test.mosquitto.org/
- broker_path (string; optional): MQTT broker path
- options (dict; optional): MQTT options (optional).
Otherwise defaults to DEFAULT_OPTIONS
- topics (list of strings; optional): MQTT topics this component is subscribed to.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- message (dict; optional): Topic or topic and payload to send.
When this property is set, a message is published
The topic is required, the payload is not.
- incoming (dict; optional): Incoming message"""
    @_explicitize_args
    def __init__(self, state=Component.UNDEFINED, broker_url=Component.UNDEFINED, protocol=Component.UNDEFINED, broker_port=Component.UNDEFINED, broker_path=Component.UNDEFINED, options=Component.UNDEFINED, topics=Component.UNDEFINED, id=Component.UNDEFINED, message=Component.UNDEFINED, incoming=Component.UNDEFINED, **kwargs):
        self._prop_names = ['state', 'broker_url', 'protocol', 'broker_port', 'broker_path', 'options', 'topics', 'id', 'message', 'incoming']
        self._type = 'DashMqtt'
        self._namespace = 'dash_mqtt'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['state', 'broker_url', 'protocol', 'broker_port', 'broker_path', 'options', 'topics', 'id', 'message', 'incoming']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashMqtt, self).__init__(**args)
