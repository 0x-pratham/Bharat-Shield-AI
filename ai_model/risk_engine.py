def calculate_risk(probability, app_data):
    risk_score = int(probability * 100)
    reasons = []

    package_name = app_data.get("package_name", "").lower()

    # --- BASE RULES ---
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

    # --- TRUST SYSTEM ---

    # Trusted apps
    if any(x in package_name for x in ["amazon", "flipkart", "google", "youtube"]):
        risk_score -= 20
        reasons.append("Trusted package detected")

    # Semi-trusted apps (third-party stores)
    elif any(x in package_name for x in ["uptodown", "apkpure", "apkmirror"]):
        risk_score -= 10
        reasons.append("Third-party app store (moderate trust)")

    # --- MISMATCH LOGIC ---
    if "calculator" in package_name and app_data["internet_access"] == 1:
        risk_score += 20
        reasons.append("Calculator app using internet (suspicious)")

    # --- FINAL ---
    risk_score = max(0, min(100, risk_score))

    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status, reasons