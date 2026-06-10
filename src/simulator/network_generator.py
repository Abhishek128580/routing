import random


def generate_network_state():

    latency = random.randint(20, 500)

    load = random.randint(10, 100)

    bandwidth = random.randint(10, 100)

    return {
        "latency": latency,
        "load": load,
        "bandwidth": bandwidth
    }