import csv
import os

LOG_FILE = "src/logs/routing_logs.csv"


def log_routing(
    query,
    domain,
    complexity,
    complexity_score,
    latency,
    load,
    route,
    processing_time
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
                "complexity",
                "complexity_score",
                "latency",
                "load",
                "route",
                "processing_time"

            ])

        writer.writerow([
           query,
            domain,
            complexity,
            complexity_score,
            latency,
            load,
            route,
            processing_time
        ])