import React, {Component} from 'react';
import mqtt from 'mqtt'
import PropTypes from 'prop-types';

const DEFAULT_OPTIONS =  {
    keepalive: 30,
    clientId:  'dash_mqtt_' + Math.random().toString(16).substr(2, 8),
    protocolId: 'MQTT',
    protocolVersion: 5,
    clean: true,
    reconnectPeriod: 1000,
    connectTimeout: 30 * 1000,
    will: {
      topic: 'WillMsg',
      payload: 'Connection Closed abnormally..!',
      qos: 0,
      retain: false
    },
    rejectUnauthorized: false
  }

const DEFAULT_PORT = 8080; //for MQTT over websockets to mosquitto
/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashMqtt extends Component {

    _initMqttClient() {
        // Create a new client.
        let {protocol} = this.props;
        let {broker_url} = this.props;
        let {options} = this.props;
        const {topics} = this.props;
        let {broker_port} = this.props;
        const {broker_path} = this.props;
        
        if (!broker_port){
            broker_port = (options && options.port) ? options.port : DEFAULT_PORT;
        }
        

        options = options ? options : DEFAULT_OPTIONS;

        protocol = protocol ? protocol : 'mqtt'
        broker_url = broker_url ? broker_url : location.host;  

        if (!broker_url.startsWith('mqtt://') && !broker_url.startsWith('mqtts://')){
            if (!['mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'].includes(protocol.toLowerCase())){
                console.error('Unsuitable protocol');
            } 
            broker_url = protocol.toLowerCase() + '://' + broker_url;
        }


        if ((broker_url.match(/:/g)||[]).length ===  1){
            broker_url = broker_url + ':' + broker_port.toString();
        }

        if(broker_path){
            broker_url = broker_url +'/'+broker_path
        }

        this.client = mqtt.connect(broker_url, options);        
        
        const self = this;

        this.client.on('connect', function (){

            for (var i = 0; i < topics.length; i++) {
                self.client.subscribe(topics[i]);
            }

            self.props.setProps({
                state: {
                    connected: true,
                    reconnecting : false
                }
            })
            
        })


        this.client.on('reconnect', function (){
            self.props.setProps({
                state: {
                    connected: false,
                    reconnecting : true
                }
            })
            
        })

        this.client.on('message', function (topic, payload, packet){

            let my_payload = payload;
            if (Buffer.isBuffer(payload)){
                my_payload = payload.toString();
            }
            self.props.setProps({
                incoming:{
                    topic: topic,
                    payload: my_payload,
                    packet: packet
                }
            })
        })

        this.client.on('error', function(error){
            console.log(error);        
        })
    }


    _whatChanged(prevProps){
        return Object.keys(this.props)
        .filter(key => {
          return prevProps[key] !== this.props[key];
        })
    }

    componentDidMount() {
        this._initMqttClient()
    }

    componentDidUpdate(prevProps) {
        
        const whatChanged = this._whatChanged(prevProps)

        const {message} = this.props;
        // Send messages, if changed.
        if (whatChanged.includes("message")) { 
            if (this.props.state.connected) {
                if (message.payload !== undefined){
                    this.client.publish(message.topic, message.payload);
                } else {
                    this.client.publish(message.topic);
                }
                
            } else if (!this.props.state.reconnecting){
                this.client.reconnect();
            }
        }
    }

    componentWillUnmount() {
        // Clean up (close the connection).
        if (this.client){
            this.client.end();
        }
   
    }

    render() {
        return (null);
    }
}

DashMqtt.defaultProps = {
    state: {
        connected : false, 
        reconnecting : false
    }
};

DashMqtt.propTypes = {


    /**
     * This MQTT connection state (in the readyState prop) and any associated information.
     */
    state: PropTypes.object,

    /**
     * The MQTT broker endpoint (e.g. 'mqtt://test.mosquitto.org'). 
     */
    broker_url: PropTypes.string,

    /**
     * One the following protocols: 'mqtt', 'mqtts', 'tcp', 'tls', 'ws', 'wss'.
     * Defaults to 'mqtt' which then is defaulted to 'ws' by MQTT.js 
     * From (https://github.com/mqttjs/MQTT.js/issues/628#issuecomment-345412483)
     * There is no way for JavaScript running in browsers to open TCP sockets so "normal" MQTT is impossible in browser apps. 
     * To get around this limitation, MQTT.js uses MQTT over WebSockets instead when it detects it's running in a browser.
     */
    protocol: PropTypes.string,

    /**
     * The MQTT broker port, defaults to 
     * Default to 8080 as MQTT over WebSockets, unencrypted as per
     * https://test.mosquitto.org/
      */
    broker_port: PropTypes.number,


    /**
     * MQTT broker path
     */
    broker_path: PropTypes.string,


    /**
     * MQTT options (optional).
     * Otherwise defaults to DEFAULT_OPTIONS
     */
    options: PropTypes.object,

    /**
     * MQTT topics this component is subscribed to.
     */
    topics: PropTypes.arrayOf(PropTypes.string),

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Topic or topic and payload to send.
     * When this property is set, a message is published
     * The topic is required, the payload is not. 
     */
    message: PropTypes.object,


    /**
     * Incoming message 
     */
    incoming:PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
