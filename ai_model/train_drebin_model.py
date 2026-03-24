import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# --- LOAD DREBIN DATASET ---
df = pd.read_csv("dataset/drebin_dataset.csv")

# --- SPLIT ---
X = df.drop("label", axis=1)
y = df["label"]

# --- TRAIN TEST SPLIT ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- MODEL ---
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42
)

# --- TRAIN ---
model.fit(X_train, y_train)

# --- EVALUATE ---
accuracy = model.score(X_test, y_test)
print(f"\n✅ Drebin Model Accuracy: {accuracy * 100:.2f}%")

y_pred = model.predict(X_test)
print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred))

# --- SAVE ---
joblib.dump(model, "model/drebin_model.pkl")

print("\n✅ Drebin model trained and saved")
print("Total samples:", len(df))