import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# --- LOAD DATASET ---
df = pd.read_csv("dataset/malware_dataset.csv")

# --- SPLIT FEATURES & LABEL (FIXED 🔥) ---
X = df.drop("label", axis=1)
y = df["label"]

# --- TRAIN-TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- MODEL (IMPROVED 🔥) ---
model = RandomForestClassifier(
    n_estimators=300,     # more trees = better learning
    max_depth=12,         # deeper understanding
    random_state=42
)

# --- TRAIN ---
model.fit(X_train, y_train)

# --- EVALUATE ---
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# --- SAVE MODEL ---
joblib.dump(model, "model/bharatshield_model.pkl")

print("✅ Model trained and saved successfully")