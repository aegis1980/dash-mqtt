# AUTO GENERATED FILE - DO NOT EDIT

''DashMqtt <- function(state=NULL, broker_url=NULL, protocol=NULL, broker_port=NULL, broker_path=NULL, options=NULL, topics=NULL, id=NULL, message=NULL, incoming=NULL) {
    
    props <- list(state=state, broker_url=broker_url, protocol=protocol, broker_port=broker_port, broker_path=broker_path, options=options, topics=topics, id=id, message=message, incoming=incoming)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMqtt',
        namespace = 'dash_mqtt',
        propNames = c('state', 'broker_url', 'protocol', 'broker_port', 'broker_path', 'options', 'topics', 'id', 'message', 'incoming'),
        package = 'dashMqtt'
        )

    structure(component, class = c('dash_component', 'list'))
}
