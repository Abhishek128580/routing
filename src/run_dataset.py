import pandas as pd

from classifier.classifier import classify_query

from scheduler.heuristic_scheduler import route_query

from simulator.simulator import LOW

from logs.logger import log_routing


df = pd.read_csv(
    "C:\\Users\\kotha\\OneDrive\\Desktop\\Intelligent-Query-Routing\\src\\data\\queries.csv"
)

for _, row in df.iterrows():

    query = row["query"]

    result = classify_query(query)

    route = route_query(
        result["complexity"],
        LOW.load
    )

    log_routing(
        query,
        result["domain"],
        result["complexity"],
        LOW.name,
        route
    )

print(
    f"Processed {len(df)} queries"
)