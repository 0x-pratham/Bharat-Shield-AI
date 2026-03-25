import pandas as pd

def extract_features(app_data, model):
    """
    Convert app_data into full feature vector matching trained model
    """

    # 🔥 Get model feature names (215 features)
    feature_names = model.feature_names_in_

    # 🔥 Start with all zeros
    features = {col: 0 for col in feature_names}

    # 🔥 Map your existing features (basic mapping)
    features["SEND_SMS"] = app_data.get("sms_permission", 0)
    features["INTERNET"] = app_data.get("internet_access", 0)
    features["RECEIVE_SMS"] = app_data.get("sms_permission", 0)
    features["READ_SMS"] = app_data.get("sms_permission", 0)

    # You can expand mapping later 🔥

    # 🔥 Convert to DataFrame
    df = pd.DataFrame([features])

    return df