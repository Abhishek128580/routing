def route_query(
    complexity,
    load
):

    if load > 80:
        return "cloud"

    if complexity == "low":
        return "device"

    elif complexity == "medium":
        return "edge"

    else:
        return "cloud"