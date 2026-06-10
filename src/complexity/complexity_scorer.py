# TECHNICAL_KEYWORDS = [
#     "algorithm",
#     "database",
#     "distributed",
#     "microservice",
#     "kubernetes",
#     "docker",
#     "network",
#     "machine learning",
#     "deep learning",
#     "neural network",
#     "compiler",
#     "operating system",
#     "dijkstra",
#     "graph",
#     "optimization"
# ]


# def calculate_complexity(query):

#     query_lower = query.lower()

#     score = 0

#     score += len(query.split())

#     for keyword in TECHNICAL_KEYWORDS:

#         if keyword in query_lower:
#             score += 5

#     if score < 15:
#         complexity = "low"

#     elif score < 30:
#         complexity = "medium"

#     else:
#         complexity = "high"

#     return {
#         "score": score,
#         "complexity": complexity
#     }

QUESTION_TYPES = {
    "what": 5,
    "who": 5,
    "when": 5,
    "where": 5,
    "why": 10,
    "how": 15,
    "implement": 20,
    "design": 30,
    "build": 30,
    "develop": 30,
    "optimize": 25,
    "analyze": 25,
    "compare": 20
}


DOMAIN_WEIGHTS = {
    "software engineering and programming": 30,
    "medicine and healthcare": 20,
    "law and legal matters": 20,
    "mathematics and statistics": 25,
    "natural science and physics": 20,
    "business finance and economics": 15,
    "general trivia and history": 5
}


def calculate_complexity(
    query,
    domain,
    confidence
):

    score = 0

    score += len(query.split())

    query_lower = query.lower()

    for keyword, value in QUESTION_TYPES.items():

        if keyword in query_lower:

            score += value
            break

    score += DOMAIN_WEIGHTS.get(
        domain,
        10
    )

    score += confidence * 20

    if score < 40:
        complexity = "low"

    elif score < 70:
        complexity = "medium"

    else:
        complexity = "high"

    return {
        "score": round(score, 2),
        "complexity": complexity
    }