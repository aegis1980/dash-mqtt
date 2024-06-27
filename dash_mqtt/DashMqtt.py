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

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- broker_path (string; optional):
    MQTT broker path.

- broker_port (number; optional):
    The MQTT broker port, defaults to  Default to 8080 as MQTT over
    WebSockets, unencrypted as per https://test.mosquitto.org/.

- broker_url (string; optional):
    The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org').

- incoming (dict; optional):
    Incoming message.

- message (dict; optional):
    Topic or topic and payload to send. When this property is set, a
    message is published The topic is required, the payload is not.

- options (dict; optional):
    MQTT options (optional). Otherwise defaults to DEFAULT_OPTIONS.

- protocol (string; optional):
    One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws',
    'wss'. Defaults to 'mqtt' which then is defaulted to 'ws' by
    MQTT.js  From
    (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
    There is no way for JavaScript running in browsers to open TCP
    sockets so \"normal\" MQTT is impossible in browser apps.  To get
    around this limitation, MQTT.js uses MQTT over WebSockets instead
    when it detects it's running in a browser.

- state (dict; default {    connected : False,     reconnecting : False}):
    This MQTT connection state (in the readyState prop) and any
    associated information.

- topics (list of strings; optional):
    MQTT topics this component is subscribed to."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_mqtt'
    _type = 'DashMqtt'
    @_explicitize_args
    def __init__(self, state=Component.UNDEFINED, broker_url=Component.UNDEFINED, protocol=Component.UNDEFINED, broker_port=Component.UNDEFINED, broker_path=Component.UNDEFINED, options=Component.UNDEFINED, topics=Component.UNDEFINED, id=Component.UNDEFINED, message=Component.UNDEFINED, incoming=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'broker_path', 'broker_port', 'broker_url', 'incoming', 'message', 'options', 'protocol', 'state', 'topics']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'broker_path', 'broker_port', 'broker_url', 'incoming', 'message', 'options', 'protocol', 'state', 'topics']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashMqtt, self).__init__(**args)
