# 🧠 Customer Churn Prediction & Retention Strategy using SQL, ML & Power BI

This project is an end-to-end solution to identify customers likely to churn and recommend retention strategies. It leverages SQL for data retrieval, machine learning for prediction, and Power BI for rich, interactive visualizations.

---

## 🚀 Project Highlights

- 💾 Data ingested from SQL Server views (`vw_ChurnData`, `vw_JoinData`)
- ⚙️ Data preprocessing and SMOTE balancing for class imbalance
- 🧪 GridSearchCV-based hyperparameter tuning across 5 models
- 📈 MLflow used for logging experiments, performance, and LIME explanations
- 📊 Final churn prediction integrated with Power BI for business insights

---

## 🔍 Objective

Predict churn probability for telecom customers and analyze churn patterns based on demographic, behavioral, and service usage features.

---

## 🧱 Machine Learning Models

Models trained with both **imbalanced** and **SMOTE-balanced** datasets:

- Logistic Regression
- Random Forest
- XGBoost
- LightGBM
- K-Nearest Neighbors

### ✅ Final Model Selected
- **Model:** LightGBM  
- **Dataset:** Balanced  
- **F1 Score (Churned Class):** 0.90

---

## 🛠️ Project Workflow

![Workflow Diagram](Power%20BI%20Dashboard/Images/Flow%20Diagram.drawio.png)

---

## 🧪 Model Training & Tracking

- Separate experiments: `Churn_Imbalanced` & `Churn_Balanced`
- Tracked via MLflow:  
  - Model performance metrics  
  - Hyperparameters  
  - Feature importance via LIME
- Metrics: Precision, Recall, F1 for each class

---

## 📊 Visualizations

### Churn Summary Dashboard
![Churn Summary Dashboard](Power%20BI%20Dashboard/Images/Summary.png)

### Churn Prediction Dashboard
![Churn Prediction Dashboard](Power%20BI%20Dashboard/Images/Predictions.png)

---

## 📤 Prediction Output

- Churn predictions made on `vw_JoinData`
- Final output merged with original data for Power BI visualization
- Exported to `data/test/Predictions.csv`

---

## 📦 Tech Stack

- Python, Scikit-learn, XGBoost, LightGBM
- Pandas, NumPy, Seaborn, Matplotlib
- MLflow, LIME, DVC
- SQL Server
- Power BI

---

## 📈 Result

With robust preprocessing and balancing techniques, **LightGBM** achieved the best performance on churn prediction. The predicted churners were integrated into a **Power BI** dashboard to support business decisions.