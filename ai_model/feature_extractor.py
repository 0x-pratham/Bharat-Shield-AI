def extract_features(app_data):
    """
    Simulated feature extractor (for now)
    Later this will come from real APK
    """

    features = [
        app_data.get("permission_count", 0),
        app_data.get("sms_permission", 0),
        app_data.get("internet_access", 0),
        app_data.get("background_services", 0),
        app_data.get("hidden_code", 0),
        app_data.get("libraries", 0)
    ]

    return features