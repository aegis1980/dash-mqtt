# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashMqtt <- function(id=NULL, broker_path=NULL, broker_port=NULL, broker_url=NULL, incoming=NULL, message=NULL, options=NULL, protocol=NULL, state=NULL, topics=NULL) {
    
    props <- list(id=id, broker_path=broker_path, broker_port=broker_port, broker_url=broker_url, incoming=incoming, message=message, options=options, protocol=protocol, state=state, topics=topics)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMqtt',
        namespace = 'dash_mqtt',
        propNames = c('id', 'broker_path', 'broker_port', 'broker_url', 'incoming', 'message', 'options', 'protocol', 'state', 'topics'),
        package = 'dashMqtt'
        )

    structure(component, class = c('dash_component', 'list'))
}
