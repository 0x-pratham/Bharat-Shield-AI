def calculate_risk(probability, app_data):
    """
    Combine ML prediction with rule-based risk scoring
    """

    # 🔥 Base AI score (0–40)
    risk_score = int(probability * 40)

    reasons = []
    behaviors = []
    explanations = []

    # --- BASIC FEATURES ---
    permission_count = app_data.get("permission_count", 0)
    sms_permission = app_data.get("sms_permission", 0)
    internet_access = app_data.get("internet_access", 0)
    background_services = app_data.get("background_services", 0)
    hidden_code = app_data.get("hidden_code", 0)

    # --- PERMISSION CHECK ---
    if permission_count > 25:
        risk_score += 5
        reasons.append("Too many permissions")

    # --- BACKGROUND SERVICES ---
    if background_services > 10:
        risk_score += 5
        reasons.append("High background activity")
        behaviors.append("Runs continuously in background")

    # --- SMS RISK ---
    if sms_permission == 1:
        risk_score += 15
        reasons.append("SMS access detected")
        behaviors.append("Can read SMS / OTP")
        explanations.append("May access sensitive messages")

    # --- INTERNET ---
    if internet_access == 1:
        reasons.append("Internet access enabled")
        behaviors.append("Can send/receive data")

    # --- HIDDEN CODE ---
    if hidden_code == 1:
        risk_score += 10
        reasons.append("Hidden behavior detected")
        behaviors.append("May perform hidden operations")

    # --- SAFE PATTERN REDUCTION ---
    if sms_permission == 0 and hidden_code == 0:
        risk_score -= 10
        reasons.append("No strong malicious indicators")

    # --- ANOMALY DETECTION ---
    anomaly_score = 0

    if hidden_code == 1:
        anomaly_score += 1

    if background_services > 15:
        anomaly_score += 1

    if permission_count > 35:
        anomaly_score += 1

    if anomaly_score >= 2:
        risk_score += 15
        reasons.append("Suspicious behavior pattern detected")
        explanations.append("Multiple unusual signals found")

    # --- FINAL CLAMP ---
    risk_score = max(0, min(100, risk_score))

    # --- FINAL STATUS ---
    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status, reasons, behaviors, explanations