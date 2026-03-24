# 🛡️ Bharat Shield AI

AI-powered Android malware detection system that analyzes APK files and predicts security risks with explainable insights.

---

## 🚀 Features

- 🔍 APK Static Analysis
- 🤖 AI-based Malware Detection
- 🧠 Risk Scoring Engine
- 🔐 Modded App Detection
- ⚠ Behavior Prediction
- 👨‍👩‍👧 User-Friendly Explanation
- 📊 Confidence Score

---

## 📂 Project Structure
BHARAT-SHIELDAI/
│
├── ai_model/
│ ├── apk_analyzer.py # Extracts APK data
│ ├── feature_extractor.py # Converts data → ML features
│ ├── risk_engine.py # Risk + logic engine
│ ├── main.py # Main execution file
│ ├── train_model.py # Model training script
│
├── dataset/
│ └── malware_dataset.csv # Training dataset
│
├── model/
│ └── bharatshield_model.pkl # Trained AI model
│
├── notebooks/
│ └── train_model.ipynb # Experimentation
│
└── README.md


---

## ⚙️ Installation

```bash
python -m pip install pandas numpy scikit-learn joblib androguard

▶️ How to Run
cd ai_model
python main.py
Select APK file → Get analysis report

🧠 Workflow
APK File
   ↓
APK Analyzer
   ↓
Feature Extractor
   ↓
AI Model Prediction
   ↓
Risk Engine
   ↓
Final Report

📊 Output Includes
Risk Score

- Status (Safe / Suspicious / Dangerous)
- Confidence %
- Reasons
- Predicted Behavior
- Permission Explanation
- Recommendation

🔥 Technologies Used
- Python 3.10
- Scikit-learn (Random Forest)
- Androguard
- Pandas
- NumPy

⚠️ Future Improvements
- Larger dataset (Drebin dataset)
- Improved accuracy with advanced features
- Real-time app monitoring
- Cloud threat intelligence integration
- Mobile app integration
-Security Features
