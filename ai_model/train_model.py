import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("dataset/malware_dataset.csv")

# Split features and target
X = df.drop("malware", axis=1)
y = df["malware"]

# Train-test split (IMPORTANT for better learning)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model (improved)
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Evaluate (optional but good)
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "model/bharatshield_model.pkl")

print("✅ Model trained and saved successfully")