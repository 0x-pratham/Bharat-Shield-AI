from tkinter import Tk, filedialog
from apk_analyzer import analyze_apk
from feature_extractor import extract_features
from risk_engine import calculate_risk
import joblib
import pandas as pd
import os

# --- LOAD MODEL ---
try:
    model = joblib.load("model/malware_model.pkl")
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

print("\n📦 Selected APK:", apk_path)
print("📄 File Name:", os.path.basename(apk_path))

# --- STEP 1: Analyze APK ---
try:
    app_data = analyze_apk(apk_path)
    print("\n🔍 Extracted App Data:", app_data)
except Exception as e:
    print("❌ APK analysis failed:", e)
    exit()

# --- STEP 2: Feature Extraction (ALIGN WITH MODEL) ---
try:
    df = extract_features(app_data, model)   # 🔥 IMPORTANT CHANGE
except Exception as e:
    print("❌ Feature extraction failed:", e)
    exit()

# --- STEP 3: AI Prediction ---
try:
    prediction = model.predict(df)
    probability = model.predict_proba(df)

    prob_score = float(probability[0][1])  # malware probability
except Exception as e:
    print("❌ Model prediction failed:", e)
    exit()

# --- STEP 4: Risk Engine ---
risk_score, status, reasons, behaviors, explanations = calculate_risk(prob_score, app_data)

# --- STEP 5: OUTPUT ---
print("\n==============================")
print("🛡️ BHARAT SHIELD AI REPORT")
print("==============================")

print("\n📊 Risk Score:", risk_score)

# 🔥 STATUS COLOR
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
print("\n📌 Reasons:")
for r in reasons:
    print("✔", r)

# Behavior
if behaviors:
    print("\n⚠ Predicted Behavior:")
    for b in behaviors:
        print("-", b)

# Explanation
if explanations:
    print("\nℹ Explanation:")
    for e in explanations:
        print("-", e)

# Recommendation
print("\n💡 Recommendation:")
if status == "Dangerous":
    print("❌ Do NOT install this app.")
elif status == "Suspicious":
    print("⚠ Install with caution.")
else:
    print("✅ App is safe to use.")

print("\n==============================")
print("📌 FINAL SUMMARY")
print("==============================")

if status == "Safe":
    print("✅ This app appears safe.")
elif status == "Suspicious":
    print("⚠ This app shows suspicious behavior.")
else:
    print("🚨 This app is HIGH RISK!")

print("\n🔥 Analysis Complete")