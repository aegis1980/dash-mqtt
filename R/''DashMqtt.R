# AUTO GENERATED FILE - DO NOT EDIT

''DashMqtt <- function(id=NULL, label=NULL, value=NULL) {
    
    props <- list(id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashMqtt',
        namespace = 'dash_mqtt',
        propNames = c('id', 'label', 'value'),
        package = 'dashMqtt'
        )

    structure(component, class = c('dash_component', 'list'))
}
