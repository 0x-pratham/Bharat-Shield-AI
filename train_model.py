import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/malware_dataset.csv")

# Features and labels
X = data.drop("malware", axis=1)
y = data["malware"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Test prediction
test_data = [[12,3,1,2,1,4]]
prediction = model.predict(test_data)

print("Prediction:", prediction)

# Save model
joblib.dump(model, "model/bharatshield_model.pkl")