# AUTO GENERATED FILE - DO NOT EDIT

export dashmqtt

"""
    dashmqtt(;kwargs...)

A DashMqtt component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `broker_path` (String; optional): MQTT broker path
- `broker_port` (Real; optional): The MQTT broker port, defaults to 
Default to 8080 as MQTT over WebSockets, unencrypted as per
https://test.mosquitto.org/
- `broker_url` (String; optional): The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org').
- `incoming` (Dict; optional): Incoming message
- `message` (Dict; optional): Topic or topic and payload to send.
When this property is set, a message is published
The topic is required, the payload is not.
- `options` (Dict; optional): MQTT options (optional).
Otherwise defaults to DEFAULT_OPTIONS
- `protocol` (String; optional): One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'.
Defaults to 'mqtt' which then is defaulted to 'ws' by MQTT.js 
From (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
To get around this limitation, MQTT.js uses MQTT over WebSockets instead when it detects it's running in a browser.
- `state` (Dict; optional): This MQTT connection state (in the readyState prop) and any associated information.
- `topics` (Array of Strings; optional): MQTT topics this component is subscribed to.
"""
function dashmqtt(; kwargs...)
        available_props = Symbol[:id, :broker_path, :broker_port, :broker_url, :incoming, :message, :options, :protocol, :state, :topics]
        wild_props = Symbol[]
        return Component("dashmqtt", "DashMqtt", "dash_mqtt", available_props, wild_props; kwargs...)
end

