import joblib
import pandas as pd

# Load model
model = joblib.load("model/malware_model.pkl")

# 🔥 Dummy test input (must match 215 features)
sample = pd.DataFrame([[0]*215])

prediction = model.predict(sample)

print("Prediction:", prediction)