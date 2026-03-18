import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/malware_dataset.csv")

# Features and label
X = data.drop("malware", axis=1)
y = data["malware"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Test prediction
sample = pd.DataFrame([[12,1,1,2,1,1]], columns=X.columns)

prediction = model.predict(sample)
probability = model.predict_proba(sample)

print("Prediction:", prediction)
print("Malware Probability:", probability[0][1])

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