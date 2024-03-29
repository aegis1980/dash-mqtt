% Auto-generated: do not edit by hand
\name{''DashMqtt}

\alias{''DashMqtt}

\title{DashMqtt component}

\description{
ExampleComponent is an example component. It takes a property, `label`, and displays it. It renders an input with the property `value` which is editable by the user.
}

\usage{
''DashMqtt(state=NULL, broker_url=NULL, protocol=NULL,
broker_port=NULL, broker_path=NULL, options=NULL,
topics=NULL, id=NULL, message=NULL, incoming=NULL)
}

\arguments{
\item{state}{Named list. This MQTT connection state (in the readyState prop) and any associated information.}

\item{broker_url}{Character. The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org').}

\item{protocol}{Character. One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'.
Defaults to 'mqtt' which then is defaulted to 'ws' by MQTT.js 
From (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
To get around this limitation, MQTT.js uses MQTT over WebSockets instead when it detects it's running in a browser.}

\item{broker_port}{Numeric. The MQTT broker port, defaults to 
Default to 8080 as MQTT over WebSockets, unencrypted as per
https://test.mosquitto.org/}

\item{broker_path}{Character. MQTT broker path}

\item{options}{Named list. MQTT options (optional).
Otherwise defaults to DEFAULT_OPTIONS}

\item{topics}{List of characters. MQTT topics this component is subscribed to.}

\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{message}{Named list. Topic or topic and payload to send.
When this property is set, a message is published
The topic is required, the payload is not.}

\item{incoming}{Named list. Incoming message}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

