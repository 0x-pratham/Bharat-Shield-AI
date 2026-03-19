from apk_analyzer import analyze_apk
from feature_extractor import extract_features
from risk_engine import calculate_risk
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/bharatshield_model.pkl")

# Give APK path here
apk_path = "sample.apk"   # put your apk file here

# Step 1: Analyze APK
app_data = analyze_apk(apk_path)

print("Extracted App Data:", app_data)

# Step 2: Convert to features
features = extract_features(app_data)

sample = pd.DataFrame([features], columns=[
    "permission_count",
    "sms_permission",
    "internet_access",
    "background_services",
    "hidden_code",
    "libraries"
])

# Step 3: Predict
prediction = model.predict(sample)
probability = model.predict_proba(sample)

# Step 4: Risk evaluation
risk_score, status, reasons = calculate_risk(probability[0][1], app_data)

print("Risk Score:", risk_score)
print("Status:", status)

print("\nReasons:")
for r in reasons:
    print("-", r)