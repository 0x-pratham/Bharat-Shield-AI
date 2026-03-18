def calculate_risk(probability):
    """
    Convert AI probability into risk score and status
    """

    risk_score = int(probability * 100)

    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status