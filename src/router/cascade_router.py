CONFIDENCE_THRESHOLD = 0.60


def cascade_decision(
    confidence
):

    if confidence >= CONFIDENCE_THRESHOLD:

        return "accept"

    return "escalate"