from pathlib import Path
import csv

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

DREBIN_COLUMNS = [
    "perm_sms",
    "perm_contacts",
    "perm_storage",
    "perm_camera",
    "internet",
    "high_background",
    "hidden_code",
    "many_permissions",
    "is_social",
    "is_payment",
    "label",
]
FEATURE_COLUMNS = DREBIN_COLUMNS[:-1]
DATASET_PATH = Path("dataset/drebin_dataset.csv")
MODEL_PATH = Path("model/drebin_model.pkl")


def validate_and_load_dataset(csv_path: Path) -> tuple[pd.DataFrame, list[str]]:
    issues = []
    cleaned_rows = []

    with csv_path.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        rows = list(reader)

    if not rows:
        raise ValueError("Dataset is empty.")

    header = [cell.strip() for cell in rows[0]]
    if header != DREBIN_COLUMNS:
        raise ValueError(
            f"Invalid header. Expected {DREBIN_COLUMNS} but found {header}."
        )

    for line_number, raw_row in enumerate(rows[1:], start=2):
        if not raw_row or not any(cell.strip() for cell in raw_row):
            issues.append(f"Skipped blank line {line_number}.")
            continue

        if len(raw_row) != len(DREBIN_COLUMNS):
            issues.append(
                f"Skipped line {line_number}: expected {len(DREBIN_COLUMNS)} fields, "
                f"found {len(raw_row)}."
            )
            continue

        row = [cell.strip() for cell in raw_row]
        try:
            parsed = [int(value) for value in row]
        except ValueError:
            issues.append(f"Skipped line {line_number}: non-integer values detected.")
            continue

        feature_values = parsed[:-1]
        label = parsed[-1]

        if any(value not in (0, 1) for value in feature_values):
            issues.append(
                f"Skipped line {line_number}: features must be binary (0 or 1)."
            )
            continue

        if label not in (0, 1, 2):
            issues.append(f"Skipped line {line_number}: label must be 0, 1, or 2.")
            continue

        cleaned_rows.append(dict(zip(DREBIN_COLUMNS, parsed)))

    df = pd.DataFrame(cleaned_rows, columns=DREBIN_COLUMNS)
    if df.empty:
        raise ValueError("No valid rows remained after cleaning the dataset.")

    return df, issues


def choose_test_size(y: pd.Series) -> tuple[float, pd.Series | None]:
    class_counts = y.value_counts().sort_index()
    if len(class_counts) < 2:
        raise ValueError("Need at least 2 classes to train a classifier.")

    min_count = int(class_counts.min())
    if min_count < 2:
        return 0.3, None

    n_classes = int(class_counts.size)
    n_samples = int(len(y))
    min_test_fraction = n_classes / n_samples
    test_size = max(0.3, min_test_fraction)
    test_size = min(test_size, 0.5)
    return test_size, y


def main() -> None:
    df, issues = validate_and_load_dataset(DATASET_PATH)
    X = df[FEATURE_COLUMNS]
    y = df["label"]

    test_size, stratify_target = choose_test_size(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=stratify_target,
    )

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        random_state=42,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    y_pred = model.predict(X_test)

    print("\nDataset summary:")
    print(f"Valid rows used: {len(df)}")
    print("Class distribution:")
    print(y.value_counts().sort_index())

    if issues:
        print("\nCleaning notes:")
        for issue in issues:
            print(f"- {issue}")

    print("\nSplit summary:")
    print(f"test_size={test_size:.2f}")
    if stratify_target is None:
        print("Stratify disabled because at least one class has fewer than 2 samples.")
    else:
        print("Stratify enabled.")
    print("Test set distribution:")
    print(y_test.value_counts().sort_index())

    print(f"\nDrebin Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, labels=[0, 1, 2], zero_division=0))

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"\nModel saved to {MODEL_PATH}")


if __name__ == "__main__":
    main()
