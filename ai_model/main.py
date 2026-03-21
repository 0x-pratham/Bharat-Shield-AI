from tkinter import Tk, filedialog
from apk_analyzer import analyze_apk
from feature_extractor import extract_features
from risk_engine import calculate_risk
import joblib
import pandas as pd
import os

# Load trained model
model = joblib.load("model/bharatshield_model.pkl")

# --- FILE PICKER (NEW 🔥) ---
Tk().withdraw()  # hide tkinter window

apk_path = filedialog.askopenfilename(
    title="Select APK file",
    filetypes=[("APK files", "*.apk")]
)

if not apk_path:
    print("❌ No file selected")
    exit()

print("Selected APK:", apk_path)
print("File Name:", os.path.basename(apk_path))


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

# Step 5: Output (FINAL REPORT)
print("\n===== BHARAT SHIELD AI REPORT =====")

print("Package:", app_data.get("package_name"))
print("Risk Score:", risk_score)
print("Status:", status)

# Confidence
confidence = probability[0][1] * 100
print(f"Confidence: {confidence:.2f}%")

print("\nReasons:")
for r in reasons:
    print("✔", r)

# Recommendation
if status.startswith("Dangerous"):
    print("\n⚠ Recommendation: Do NOT install this app.")
elif status.startswith("Suspicious"):
    print("\n⚠ Recommendation: Install with caution.")
else:
    print("\n✅ Recommendation: App is safe to use.")