def calculate_risk(probability, app_data):
    # Balanced AI weight
    risk_score = int(probability * 70)
    reasons = []

    package_name = app_data.get("package_name", "").lower()

    # --- BASE RULES ---
    if app_data["permission_count"] > 25:
        risk_score += 5
        reasons.append("Too many permissions")

    if app_data["background_services"] > 10:
        reasons.append("ℹ App runs in background which may consume battery or track activity")
        risk_score += 5
        reasons.append("High background activity")

    if app_data["sms_permission"] == 1:
        risk_score += 15
        reasons.append("SMS access detected (high risk)")

    if app_data["internet_access"] == 1:
        reasons.append("Internet access detected")

# 🔥 ADD THIS BELOW
    if app_data["internet_access"] == 1:
     reasons.append("ℹ Internet is used for loading content or communication (normal)")

    # --- IMPROVED HIDDEN CODE LOGIC ---
    if app_data["hidden_code"] == 1 and app_data["sms_permission"] == 1:
        risk_score += 10
        reasons.append("Hidden behavior with SMS access (high risk)")
    elif app_data["hidden_code"] == 1:
        risk_score += 2
        reasons.append("Complex internal behavior detected")

    # --- PERMISSION INTELLIGENCE ---
    if app_data["internet_access"] == 1 and app_data["sms_permission"] == 0:
        risk_score -= 10
        reasons.append("Internet usage is normal for most apps")

    # --- NORMAL APP RELAXATION ---
    if app_data["sms_permission"] == 0 and app_data["hidden_code"] == 0:
        risk_score -= 10
        reasons.append("No critical malicious indicators")

    # --- TRUST SCORE SYSTEM ---
    trust_score = 0

    if app_data["sms_permission"] == 0:
        trust_score += 2

    if app_data["hidden_code"] == 0:
        trust_score += 1

    if app_data["background_services"] < 10:
        trust_score += 1

    if app_data["sms_permission"] == 1:
        reasons.append("⚠ Can read SMS messages (may access OTP)")
        trust_score -= 3

    if app_data["hidden_code"] == 1 and app_data["background_services"] > 10:
        trust_score -= 2

    risk_score -= trust_score * 4
    reasons.append(f"Trust score adjustment: {trust_score}")

    # --- MODDED / UNOFFICIAL APP DETECTION 🔥 ---
    if any(keyword in package_name for keyword in ["mod", "pro", "hack", "plus", "clone"]):
        risk_score += 20
        reasons.append("Possible unofficial or modified app detected")

    # --- MISMATCH LOGIC ---
    if "calculator" in package_name and app_data["internet_access"] == 1:
        risk_score += 20
        reasons.append("Calculator app using internet (suspicious)")

    # --- FINAL CLAMP ---
    risk_score = max(0, min(100, risk_score))

    # --- STATUS ---
    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status, reasons