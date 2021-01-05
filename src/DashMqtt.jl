
module DashMqtt
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("''_dashmqtt.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "dash_mqtt",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "dash_mqtt.min.js",
    external_url = "https://unpkg.com/dash_mqtt@0.0.1/dash_mqtt/dash_mqtt.min.js",
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "dash_mqtt.min.js.map",
    external_url = "https://unpkg.com/dash_mqtt@0.0.1/dash_mqtt/dash_mqtt.min.js.map",
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
