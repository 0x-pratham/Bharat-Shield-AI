def extract_drebin_features(app_data):
    features = {}

    package_name = app_data.get("package_name", "").lower()

    # --- PERMISSION FEATURES (ADAPTED 🔥) ---
    # Since we don't have raw permission list, we use available data

    features["perm_sms"] = app_data.get("sms_permission", 0)

    # Estimate other permissions from count
    permission_count = app_data.get("permission_count", 0)

    features["perm_contacts"] = 1 if permission_count > 20 else 0
    features["perm_storage"] = 1 if permission_count > 15 else 0
    features["perm_camera"] = 1 if permission_count > 10 else 0

    # --- NETWORK ---
    features["internet"] = app_data.get("internet_access", 0)

    # --- BEHAVIOR ---
    background = app_data.get("background_services", 0)
    features["high_background"] = 1 if background > 10 else 0

    features["hidden_code"] = app_data.get("hidden_code", 0)

    # --- COMPLEXITY ---
    features["many_permissions"] = 1 if permission_count > 30 else 0

    # --- APP TYPE ---
    features["is_social"] = 1 if any(x in package_name for x in [
        "instagram", "facebook", "whatsapp", "telegram", "discord"
    ]) else 0

    features["is_payment"] = 1 if any(x in package_name for x in [
        "upi", "pay", "bank", "gpay", "phonepe", "bhim"
    ]) else 0

    return features