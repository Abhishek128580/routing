TECHNICAL_KEYWORDS = [
    "algorithm",
    "database",
    "distributed",
    "microservice",
    "kubernetes",
    "docker",
    "network",
    "machine learning",
    "deep learning",
    "neural network",
    "compiler",
    "operating system",
    "dijkstra",
    "graph",
    "optimization"
]


def calculate_complexity(query):

    query_lower = query.lower()

    score = 0

    score += len(query.split())

    for keyword in TECHNICAL_KEYWORDS:

        if keyword in query_lower:
            score += 5

    if score < 15:
        complexity = "low"

    elif score < 30:
        complexity = "medium"

    else:
        complexity = "high"

    return {
        "score": score,
        "complexity": complexity
    }