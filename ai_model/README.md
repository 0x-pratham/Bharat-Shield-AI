🛡️ Bharat Shield AI
An AI-powered Android malware detection system that analyzes APK files and predicts security risks using machine learning + behavioral analysis + explainable AI.

🚀 Features
🔍 APK Static Analysis (using Androguard)
🤖 AI-based Malware Detection (Random Forest)
🧠 Hybrid Risk Scoring Engine (AI + Rules)
🔐 Modded App Detection (Unofficial / Tampered Apps)

⚠ Behavior Prediction (What app might do)
📊 Confidence Score
🧾 Explainable AI Output (User-friendly explanations)
🧪 Drebin-inspired Feature System (Advanced pipeline)

🧠 System Architecture

APK File
   ↓
APK Analyzer (Androguard)
   ↓
Feature Extraction (Basic + Drebin-style)
   ↓
AI Model Prediction
   ↓
Risk Engine (Context-aware logic)
   ↓
Final Report (Explainable Output)

📂 Project Structure

BHARAT-SHIELDAI/
│
├── ai_model/
│   ├── apk_analyzer.py              # Extract APK data
│   ├── feature_extractor.py         # Basic ML features (6 features)
│   ├── drebin_feature_extractor.py  # Advanced Drebin-style features 🔥
│   ├── risk_engine.py               # Risk scoring + logic engine
│   ├── build_drebin_dataset.py      # Dataset builder (GUI file picker)
│   ├── train_model.py               # Basic model training
│   ├── train_drebin_model.py        # Drebin model training 🔥
│   ├── main.py                      # Main execution file
│
├── dataset/
│   ├── malware_dataset.csv          # Basic dataset (old system)
│   ├── drebin_dataset.csv           # Advanced dataset (new system) 🔥
│
├── model/
│   ├── bharatshield_model.pkl       # Basic trained model
│   ├── drebin_model.pkl             # Advanced Drebin model 🔥
│
├── notebooks/
│   └── train_model.ipynb            # Experimentation
│
└── README.md

⚙️ Installation
python -m pip install pandas numpy scikit-learn joblib androguard

▶️ How to Run
cd ai_model
python main.py

🧪 Build Drebin Dataset (New 🔥)
python build_drebin_dataset.py

Select APK via file picker

Choose label:

0 = Safe
1 = Suspicious (Mod APK)
2 = Malware
👉 Automatically saves features to drebin_dataset.csv

🤖 Train Models
🔹 Basic Model
python train_model.py

🔥 Drebin Model (Advanced)
python train_drebin_model.py

📊 Output Includes
Risk Score (0–100)

Status:

🟢 Safe

🟡 Suspicious

🔴 Dangerous

Confidence %
Reasons (Why flagged)
Predicted Behavior
Permission Explanation
Final Recommendation

🧠 AI Models
🔹 Basic Model
Uses 6 core features:

Permissions
SMS access
Internet usage
Background services
Hidden code
Libraries

🔥 Drebin-Inspired Model (Advanced)
Uses extended behavioral features:

Permission patterns
App category detection
Background behavior
Hidden logic detection
Complexity indicators

⚠️ Note:
This is a Drebin-inspired implementation, not full 123k feature Drebin dataset.
Full Drebin integration is planned as a future upgrade.

🧠 Multi-Class Classification (NEW 🔥)
Model supports:

0 → Safe
1 → Suspicious (Mod / Unofficial)
2 → Malware

👉 This improves real-world detection accuracy.

🔥 Technologies Used
Python 3.10

Scikit-learn (Random Forest)
Androguard
Pandas
NumPy
Tkinter (File Picker UI)

⚠️ Limitations
Limited dataset (currently small-scale training)
Drebin features are simplified (not full dataset)
No real-time monitoring yet
Static analysis only (no dynamic runtime analysis)

🚀 Future Improvements
Full Drebin dataset integration (5560 apps, 123k features)

Signature verification system (detect fake apps)
Real-time app monitoring (Android integration)
Backend API + cloud intelligence
Mobile app (React Native)
Dynamic malware analysis (sandboxing)
Threat intelligence database

🏆 Project Vision
To build a real-time AI-powered mobile security system that can:

Detect malware before installation
Identify fake/modded apps
Provide simple explanations for non-technical users
Work efficiently even on low-end devices

💀 FINAL NOTE
This project combines:
✔ Machine Learning
✔ Cybersecurity Concepts
✔ Explainable AI
✔ Real-world Risk Analysis

👨‍💻 Author
Akash Lad