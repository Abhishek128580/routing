import csv
import os

LOG_FILE = "src/logs/routing_logs.csv"


def log_routing(
    query,
    domain,
    bart_confidence,
    complexity,
    complexity_score,
    latency,
    load,
    route_score,
    route
):

    file_exists = os.path.exists(LOG_FILE)

    with open(
        LOG_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        if not file_exists:

            writer.writerow([
           "query",
                "domain",
                "bart_confidence",
                "complexity",
                "complexity_score",
                "latency",
                "load",
                "route_score",
                "route"

            ])

        writer.writerow([
            query,
            domain,
            bart_confidence,
            complexity,
            complexity_score,
            latency,
            load,
            route_score,
            route
        ])