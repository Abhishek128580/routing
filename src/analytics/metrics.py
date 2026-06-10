def estimate_processing_time(
    route,
    latency
):

    if route == "device":

        return latency + 50

    elif route == "edge":

        return latency + 100

    else:

        return latency + 200