from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 📂 PATHS
DATASET_PATH = Path("dataset/raw_dataset.csv")
MODEL_PATH = Path("model/malware_model.pkl")


# 🚀 LOAD + CLEAN DATASET
def load_dataset(csv_path: Path):
    df = pd.read_csv(csv_path, low_memory=False)

    # 🔥 Fix labels FIRST (VERY IMPORTANT)
    df["class"] = df["class"].map({
        "B": 0,   # Benign
        "S": 1    # Malware
    })

    # 🔥 Replace '?' with 0
    df.replace("?", 0, inplace=True)

    # 🔥 Separate features and label
    X = df.drop("class", axis=1)
    y = df["class"]

    # 🔥 Convert features to numeric
    X = X.apply(pd.to_numeric, errors='coerce')
    X.fillna(0, inplace=True)

    # 🔥 Drop any rows where label became NaN
    valid_idx = y.notna()
    X = X[valid_idx]
    y = y[valid_idx]

    print("\n✅ Dataset loaded & cleaned successfully")
    print("Shape:", X.shape)
    print("Total features:", X.shape[1])

    return X, y


def main():
    # 🧠 LOAD
    X, y = load_dataset(DATASET_PATH)

    print("\n📊 Class distribution:")
    print(y.value_counts())

    # 🚀 TRAIN TEST SPLIT
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y
    )

    print("\n📊 Test set distribution:")
    print(y_test.value_counts())

    # 🤖 MODEL
    model = RandomForestClassifier(
        n_estimators=500,
        max_depth=None,
        min_samples_split=5,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    )

    # 🚀 TRAIN
    model.fit(X_train, y_train)

    # 📊 EVALUATE
    accuracy = model.score(X_test, y_test)
    y_pred = model.predict(X_test)

    print(f"\n✅ Model Accuracy: {accuracy * 100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    # 💾 SAVE MODEL
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"\n✅ Model saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()