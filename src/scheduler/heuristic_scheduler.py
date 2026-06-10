# # def route_query(
# #     complexity,
# #     load
# # ):

# #     if load > 80:
# #         return "cloud"

# #     if complexity == "low":
# #         return "device"

# #     elif complexity == "medium":
# #         return "edge"

# #     else:
# #         return "cloud"

# def route_query(
#     complexity,
#     latency,
#     load
# ):

#     if load > 85:
#         return "cloud"

#     if latency > 300:
#         return "device"

#     if complexity == "low":
#         return "device"

#     elif complexity == "medium":
#         return "edge"

#     else:
#         return "cloud"

def calculate_route_score(
    complexity_score,
    latency,
    load,
    confidence
):

    route_score = 0

    route_score += complexity_score

    route_score += load * 0.3

    route_score += latency * 0.05

    route_score += confidence * 10

    return round(route_score, 2)


def route_query(
    route_score
):

    if route_score < 60:

        return "device"

    elif route_score < 100:

        return "edge"

    else:

        return "cloud"