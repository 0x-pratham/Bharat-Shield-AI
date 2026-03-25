import csv
from tkinter import Tk, filedialog
from apk_analyzer import analyze_apk
from drebin_feature_extractor import extract_drebin_features

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

    # Add label
    features["label"] = label

    # --- SAVE TO CSV ---
    file_path = "dataset/drebin_dataset.csv"

    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=features.keys())

        # Write header only if file is empty
        if f.tell() == 0:
            writer.writeheader()

        writer.writerow(features)

    print("✅ Data added to Drebin dataset")

except Exception as e:
    print("❌ Error:", e)