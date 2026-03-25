import csv
from tkinter import Tk, filedialog
from apk_analyzer import analyze_apk
from drebin_feature_extractor import extract_drebin_features

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

# --- FILE PICKER (🔥 NEW) ---
Tk().withdraw()

apk_path = filedialog.askopenfilename(
    title="Select APK file",
    filetypes=[("APK files", "*.apk")]
)

if not apk_path:
    print("❌ No file selected")
    exit()

print("Selected APK:", apk_path)

# --- LABEL INPUT ---
print("\nSelect App Type:")
print("0 = Safe")
print("1 = Suspicious (Mod APK)")
print("2 = Malware")

label = int(input("Enter label (0 / 1 / 2): "))

# Validate input
if label not in [0, 1, 2]:
    print("❌ Invalid label. Please enter 0, 1, or 2.")
    exit()

try:
    app_data = analyze_apk(apk_path)
    features = extract_drebin_features(app_data)

    # Force a stable schema for every appended row.
    row = {column: int(features.get(column, 0)) for column in DREBIN_COLUMNS[:-1]}
    row["label"] = label

    # --- SAVE TO CSV ---
    file_path = "dataset/drebin_dataset.csv"

    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DREBIN_COLUMNS)

        # Write header only if file is empty
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow(row)

    print("✅ Data added to Drebin dataset")

except Exception as e:
    print("❌ Error:", e)
