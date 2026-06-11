def calculate_route_score(
    complexity_score,
    latency,
    load,
    confidence
):

    route_score = 0

    route_score += complexity_score

    route_score += load * 0.15

    route_score += latency * 0.02

    route_score += confidence * 15

    return round(route_score, 2)


def route_query(
    route_score
):

    if route_score < 45:

        return "device"

    elif route_score < 85:

        return "edge"

    else:

        return "cloud"