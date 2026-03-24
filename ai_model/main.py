from tkinter import Tk, filedialog
from apk_analyzer import analyze_apk
from feature_extractor import extract_features
from drebin_feature_extractor import extract_drebin_features
from risk_engine import calculate_risk
import joblib
import pandas as pd
import os

# --- LOAD MODEL ---
try:
    model = joblib.load("model/bharatshield_model.pkl")
except Exception as e:
    print("❌ Failed to load model:", e)
    exit()

# --- FILE PICKER ---
Tk().withdraw()

apk_path = filedialog.askopenfilename(
    title="Select APK file",
    filetypes=[("APK files", "*.apk")]
)

if not apk_path:
    print("❌ No file selected")
    exit()

print("\nSelected APK:", apk_path)
print("File Name:", os.path.basename(apk_path))

# --- STEP 1: Analyze APK ---
try:
    app_data = analyze_apk(apk_path)
    print("\nExtracted App Data:", app_data)
except Exception as e:
    print("❌ APK analysis failed:", e)
    exit()

# --- STEP 2: Feature Extraction ---
try:
    features = extract_features(app_data)
except Exception as e:
    print("❌ Feature extraction failed:", e)
    exit()
    # --- NEW: DREBIN FEATURE EXTRACTION (TEST ONLY 🔥) ---
try:
    drebin_features = extract_drebin_features(app_data)
    print("\n🔬 Drebin Features:", drebin_features)
except Exception as e:
    print("❌ Drebin feature extraction failed:", e)

sample = pd.DataFrame([features], columns=[
    "permission_count",
    "sms_permission",
    "internet_access",
    "background_services",
    "hidden_code",
    "libraries"
])

# --- STEP 3: AI Prediction ---
try:
    prediction = model.predict(sample)
    probability = model.predict_proba(sample)
    prob_score = float(probability[0][1])
except Exception as e:
    print("❌ Model prediction failed:", e)
    exit()

# --- STEP 4: Risk Engine ---
risk_score, status, reasons, behaviors, explanations = calculate_risk(prob_score, app_data)

# --- STEP 5: OUTPUT ---
print("\n===== BHARAT SHIELD AI REPORT =====")

print("Package:", app_data.get("package_name", "Unknown"))
print("Risk Score:", risk_score)
    # 🔥 COLOR SYSTEM
if status == "Safe":
    print("Status: 🟢 Safe")
elif status == "Suspicious":
    print("Status: 🟡 Suspicious")
else:
    print("Status: 🔴 Dangerous")

# Confidence
confidence = prob_score * 100
print(f"Confidence: {confidence:.2f}%")

# Reasons
print("\nReasons:")
for r in reasons:
    print("✔", r)

# Behavior
if behaviors:
    print("\nPredicted Behavior:")
    for b in behaviors:
        print("⚠", b)

# Explanation
if explanations:
    print("\nPermission Explanation:")
    for e in explanations:
        print("ℹ", e)

# Recommendation
if status.startswith("Dangerous"):
    print("\n⚠ Recommendation: Do NOT install this app.")
elif status.startswith("Suspicious"):
    print("\n⚠ Recommendation: Install with caution.")
else:
    print("\n✅ Recommendation: App is safe to use.")

print("\n===== FINAL SUMMARY =====")

if status == "Safe":
    print("✅ This app appears safe based on current analysis.")
elif status == "Suspicious":
    print("⚠ This app shows some suspicious behavior. Review carefully.")
else:
    print("🚨 This app is highly risky and may harm your device or data.")