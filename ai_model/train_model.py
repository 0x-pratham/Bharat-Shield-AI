import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from feature_extractor import extract_features

# Load dataset
data = pd.read_csv("dataset/malware_dataset.csv")

# Features and label
X = data.drop("malware", axis=1)
y = data["malware"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Test prediction
# Test prediction using dynamic app data

app_data = {
    "permission_count": 12,
    "sms_permission": 1,
    "internet_access": 1,
    "background_services": 2,
    "hidden_code": 1,
    "libraries": 1
}

features = extract_features(app_data)

sample = pd.DataFrame([features], columns=X.columns)

prediction = model.predict(sample)
probability = model.predict_proba(sample)

# Convert to risk score
risk_score = int(probability[0][1] * 100)

if risk_score > 70:
    status = "Dangerous"
elif risk_score > 40:
    status = "Suspicious"
else:
    status = "Safe"

print("Risk Score:", risk_score)
print("Status:", status)

# Save model
joblib.dump(model, "model/bharatshield_model.pkl")