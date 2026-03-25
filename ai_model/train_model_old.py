import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# --- LOAD DATASET ---
df = pd.read_csv("dataset/malware_dataset.csv")

# --- SPLIT FEATURES & LABEL ---
X = df.drop("label", axis=1)
y = df["label"]

# --- TRAIN-TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- MODEL (FINAL TUNED 🔥) ---
model = RandomForestClassifier(
    n_estimators=400,      # stronger model
    max_depth=15,          # deeper understanding
    min_samples_split=2,
    random_state=42
)

# --- TRAIN ---
model.fit(X_train, y_train)

# --- EVALUATE ---
accuracy = model.score(X_test, y_test)
print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")

# 🔥 Detailed report (NEW)
y_pred = model.predict(X_test)
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# --- SAVE MODEL ---
joblib.dump(model, "model/bharatshield_model.pkl")

print("\n✅ Model trained and saved successfully")