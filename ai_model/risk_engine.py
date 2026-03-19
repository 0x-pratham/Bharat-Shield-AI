def calculate_risk(probability, app_data, apk_path):
    risk_score = int(probability * 100)
    reasons = []

    app_name = apk_path.lower()

    # --- Base Rules ---
    if app_data["permission_count"] > 25:
        risk_score += 5
        reasons.append("Too many permissions")

    if app_data["background_services"] > 10:
        risk_score += 5
        reasons.append("High background activity")

    if app_data["sms_permission"] == 1:
        risk_score += 15
        reasons.append("SMS access detected")

    if app_data["internet_access"] == 1:
        reasons.append("Uses internet connection")

    if app_data["hidden_code"] == 1:
        risk_score += 5
        reasons.append("Suspicious hidden behavior")

    # --- CONTEXT AWARE (VERY IMPORTANT) ---

    # Trusted apps (basic logic)
    if any(x in app_name for x in ["amazon", "flipkart", "google", "youtube"]):
        risk_score -= 20
        reasons.append("Trusted app category detected")

    # Suspicious mismatch logic
    if "calculator" in app_name and app_data["internet_access"] == 1:
        risk_score += 20
        reasons.append("Calculator app using internet (suspicious)")

    # Clamp
    risk_score = max(0, min(100, risk_score))

    # Status
    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status, reasons