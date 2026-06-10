# def route_query(
#     complexity,
#     load
# ):

#     if load > 80:
#         return "cloud"

#     if complexity == "low":
#         return "device"

#     elif complexity == "medium":
#         return "edge"

#     else:
#         return "cloud"

def route_query(
    complexity,
    latency,
    load
):

    if load > 85:
        return "cloud"

    if latency > 300:
        return "device"

    if complexity == "low":
        return "device"

    elif complexity == "medium":
        return "edge"

    else:
        return "cloud"