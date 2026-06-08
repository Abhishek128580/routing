class NetworkScenario:

    def __init__(self, name, latency, load):

        self.name = name
        self.latency = latency
        self.load = load


LOW = NetworkScenario(
    "LOW",
    latency=20,
    load=20
)

MEDIUM = NetworkScenario(
    "MEDIUM",
    latency=100,
    load=60
)

HIGH = NetworkScenario(
    "HIGH",
    latency=300,
    load=90
)