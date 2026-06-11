from llm.edge_llm import (
    generate_response
)

from cloud.gemini_client import (
    generate_cloud_response
)


def execute_route(
    route,
    query
):

    if route == "device":

        return {
            "tier": "device",
            "response":
            "Handled Locally"
        }

    elif route == "edge":

        result = generate_response(
            query
        )

        return {
            "tier": "edge",
            "response":
            result["response"]
        }

    else:

        response = (
            generate_cloud_response(
                query
            )
        )

        return {
            "tier": "cloud",
            "response":
            response
        }