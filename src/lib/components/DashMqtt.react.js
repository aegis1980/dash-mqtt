import React, {Component} from 'react';
import mqtt from 'mqtt'
import PropTypes from 'prop-types';

const DEFAULT_PORT = 1883;
/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashMqtt extends Component {

    _init_mqtt_client() {
        // Create a new client.
        let {broker_url} = this.props;
        let {broker_port} = this.props;
        const {options} = this.props;
        const {subscriptions} = this.props;

        broker_url = broker_url ? broker_url : "http://" + location.host;
        broker_port = broker_port ? broker_port : DEFAULT_PORT;



        this.client = mqtt.connect(broker_url + ':' + broker_port);
        
        const self = this;

        this.client.on('connect', function (){
            for (var s in subscriptions){
                self.client.subscribe(s);
            }

            self.props.setProps({
                state: {
                    connected: true
                }
            })
            
        })

        this.client.on('message', function (topic, payload){
            self.props.set({
                incoming:{
                    topic: topic,
                    payload: payload,
                    timestamp: Date.now()
                }
            })
        })

    }

    componentDidMount() {
        this._init_mqtt_client()
    }

    componentDidUpdate(prevProps) {
        const {publish} = this.props;
        // Send messages.
        if (publish) {
            if (this.props.state.connected) {
                if (publish.message){
                    this.client.publish(publish.topic, publish.message);
                } else {
                    this.client.publish(publish.topic);
                }
                
            }
        }
    }

    componentWillUnmount() {
        // Clean up (close the connection).
        this.client.end();
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
     * Defaults to 0.0.0.0 (localhost)
     */
    broker_url: PropTypes.string,

    /**
     * The MQTT broker port, defaults to 
     * Default to 1883
      */
    broker_port: PropTypes.number,

    /**
     * Client Id (required)
     */
    client_id: PropTypes.string.isRequired,

    /**
     * MQTT options (optional).
     */
    options: PropTypes.object,

    /**
     * MQTT topic subscriptions.
     */
    subscriptions: PropTypes.arrayOf(PropTypes.string),

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Topic or topic and message to send.
     * When this property is set, a message is published
     */
    publish: PropTypes.object,


    /**
     * Incoming
     */
    incoming:PropTypes.object,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
