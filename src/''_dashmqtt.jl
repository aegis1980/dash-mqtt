# AUTO GENERATED FILE - DO NOT EDIT

export ''_dashmqtt

"""
    ''_dashmqtt(;kwargs...)

A DashMqtt component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `state` (Dict; optional): This MQTT connection state (in the readyState prop) and any associated information.
- `broker_url` (String; optional): The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org'). 
Defaults to 0.0.0.0 (localhost)
- `protocol` (String; optional): One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'.
Defaults to 'mqtt' which then is defaulted to 'ws' by MQTT.js 
From (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
To get around this limitation, MQTT.js uses MQTT over WebSockets instead when it detects it's running in a browser.
- `broker_port` (Real; optional): The MQTT broker port, defaults to 
Default to 9001
- `options` (Dict; optional): MQTT options (optional).
- `topics` (Array of Strings; optional): MQTT topics this component is subscribed to.
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `message` (Dict; optional): Topic or topic and payload to send.
When this property is set, a message is published
The topic is required, the payload is not.
- `incoming` (Dict; optional): Incoming message
"""
function ''_dashmqtt(; kwargs...)
        available_props = Symbol[:state, :broker_url, :protocol, :broker_port, :options, :topics, :id, :message, :incoming]
        wild_props = Symbol[]
        return Component("''_dashmqtt", "DashMqtt", "dash_mqtt", available_props, wild_props; kwargs...)
end

