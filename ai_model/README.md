# 🛡️ Bharat Shield AI

AI-powered Android malware detection system that analyzes APK files and predicts security risks using Machine Learning, Behavioral Analysis, and Explainable AI.

---

## 🚀 Features

- APK Static Analysis (Androguard)
- AI-based Malware Detection (Random Forest)
- Hybrid Risk Scoring Engine (AI + Rules)
- Modded App Detection
- Behavior Prediction
- Confidence Score
- Explainable Output
- Drebin-inspired Feature System (Advanced)

---

## 🧠 System Workflow

APK File  
↓  
APK Analyzer  
↓  
Feature Extraction (Basic + Drebin)  
↓  
AI Model  
↓  
Risk Engine  
↓  
Final Report  

---

## 📂 Project Structure

BHARAT-SHIELDAI/

ai_model/  
 apk_analyzer.py  
 feature_extractor.py  
 drebin_feature_extractor.py  
 risk_engine.py  
 build_drebin_dataset.py  
 train_model.py  
 train_drebin_model.py  
 main.py  

dataset/  
 malware_dataset.csv  
 drebin_dataset.csv  

model/  
 bharatshield_model.pkl  
 drebin_model.pkl  

notebooks/  
 train_model.ipynb  

README.md  

---

## ⚙️ Installation

pip install pandas numpy scikit-learn joblib androguard

---

## ▶️ Run Project

cd ai_model  
python main.py  

Select APK file → Get analysis report  

---

## 🧪 Build Drebin Dataset

python build_drebin_dataset.py  

Labels:  
0 = Safe  
1 = Suspicious (Mod APK)  
2 = Malware  

---

## 🤖 Train Models

Basic Model:  
python train_model.py  

Drebin Model:  
python train_drebin_model.py  

---

## 🧠 AI Models

Basic Model:
- 6 core features
- Lightweight

Drebin Model:
- Behavioral features
- Permission patterns
- App classification
- Complexity detection

Note:
This is a Drebin-inspired system (not full dataset yet)

---

## 🧠 Multi-Class Classification

0 = Safe  
1 = Suspicious  
2 = Malware  

---

## 📊 Output Includes

- Risk Score (0–100)
- Status (Safe / Suspicious / Dangerous)
- Confidence %
- Reasons
- Predicted Behavior
- Explanation
- Recommendation

---

## ⚠️ Limitations

- Small dataset
- Simplified Drebin features
- Static analysis only
- No real-time monitoring

---

## 🚀 Future Improvements

- Full Drebin dataset integration
- Signature verification
- Real-time monitoring
- Cloud threat intelligence
- Mobile app integration
- Dynamic analysis

---

## 👨‍💻 Author

Akash Lad

---

## ⭐ Note

This project combines:
- Machine Learning
- Cybersecurity
- Explainable AI
- Risk Analysis

Making it a strong hackathon-level and industry-ready foundation.