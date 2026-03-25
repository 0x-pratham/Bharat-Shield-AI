def calculate_risk(probability, app_data):
    # 🔥 Balanced AI weight (important fix)
    risk_score = int(probability * 40)

    reasons = []
    behaviors = []
    explanations = []

    package_name = app_data.get("package_name", "").lower()

    # --- APP CATEGORY DETECTION ---
    if any(x in package_name for x in ["upi", "pay", "bank", "gpay", "phonepe", "bhim"]):
        app_category = "payment"
    elif any(x in package_name for x in ["instagram", "facebook", "telegram", "whatsapp", "discord"]):
        app_category = "social"
    elif any(x in package_name for x in ["irctc", "gov", "rail"]):
        app_category = "government"
    else:
        app_category = "general"

    # --- BASE RULES ---
    if app_data["permission_count"] > 25:
        risk_score += 5
        reasons.append("Too many permissions")

    # --- BACKGROUND LOGIC ---
    if app_data["background_services"] > 10:
        if app_category in ["social", "payment"]:
            reasons.append("Background activity is normal for this app type")
            explanations.append("Apps like social/payment apps run in background for updates")
        else:
            risk_score += 5
            reasons.append("High background activity")
            behaviors.append("Runs continuously in background")
            explanations.append("App may track activity or consume battery")

    # --- SMS LOGIC ---
    if app_data["sms_permission"] == 1:
        if app_category == "payment":
            reasons.append("SMS used for OTP verification (normal)")
            explanations.append("Payment apps use SMS for secure OTP verification")
        else:
            risk_score += 15
            reasons.append("SMS access detected (high risk)")
            behaviors.append("Can read SMS and OTP messages")
            explanations.append("App can access your messages")

    # --- INTERNET ---
    if app_data["internet_access"] == 1:
        reasons.append("Internet access detected")
        behaviors.append("Can send/receive data")
        explanations.append("App communicates with servers")

    # --- HIDDEN CODE ---
    if app_data["hidden_code"] == 1 and app_data["sms_permission"] == 1:
        if app_category == "payment":
            reasons.append("Secure processing for transactions (normal)")
            explanations.append("Encryption/security logic in payment apps")
        else:
            risk_score += 10
            reasons.append("Hidden behavior with SMS (high risk)")
            behaviors.append("Hidden operations with sensitive access")
            explanations.append("App may hide malicious activity")

    elif app_data["hidden_code"] == 1:
        risk_score += 2
        reasons.append("Complex internal behavior detected")

    # --- PERMISSION INTELLIGENCE ---
    if app_data["internet_access"] == 1 and app_data["sms_permission"] == 0:
        risk_score -= 10
        reasons.append("Internet usage is normal")

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

    if app_data["sms_permission"] == 1 and app_category == "general":
        trust_score -= 2

    if app_data["hidden_code"] == 1 and app_data["background_services"] > 10:
        trust_score -= 2

    risk_score -= trust_score * 4
    reasons.append(f"Trust score adjustment: {trust_score}")

    # ===============================
    # 🔥 ANOMALY DETECTION (NEW ADD)
    # ===============================
    anomaly_score = 0

    if app_data["hidden_code"] == 1:
        anomaly_score += 1

    if app_data["background_services"] > 15:
        anomaly_score += 1

    if app_data["permission_count"] > 35:
        anomaly_score += 1

    if anomaly_score >= 2:
        risk_score += 15
        reasons.append("Unusual behavior pattern detected")
        explanations.append("App shows abnormal combination of behaviors")

    # --- 🔥 STRONG MOD DETECTION ---
    mod_keywords = [
        "mod", "pro", "hack", "plus", "clone",
        "premium", "unlocked", "cracked", "vip"
    ]

    if any(keyword in package_name for keyword in mod_keywords):
        risk_score += 30
        reasons.append("Modified/unofficial app detected")
        behaviors.append("May bypass security restrictions")
        explanations.append("App may be altered from original")

    # --- 🔥 OFFICIAL PACKAGE CHECK ---
    official_apps = {
        "instagram": "com.instagram.android",
        "whatsapp": "com.whatsapp",
        "facebook": "com.facebook.katana"
    }

    for app, official_pkg in official_apps.items():
        if app in package_name and package_name != official_pkg:
            risk_score += 25
            reasons.append("Package mismatch (possible fake app)")
            explanations.append("App may not be from official developer")

    # --- 🔥 WHITELIST (SAFE APPS) ---
    safe_apps = [
        "com.instagram.android",
        "com.whatsapp",
        "com.google.android.youtube",
        "in.org.npci.upiapp"
    ]

    if package_name in safe_apps:
        risk_score -= 25
        reasons.append("Verified official application")

    # --- FINAL CLAMP ---
    risk_score = max(0, min(100, risk_score))

    # --- STATUS ---
    if risk_score > 70:
        status = "Dangerous"
    elif risk_score > 40:
        status = "Suspicious"
    else:
        status = "Safe"

    return risk_score, status, reasons, behaviors, explanations