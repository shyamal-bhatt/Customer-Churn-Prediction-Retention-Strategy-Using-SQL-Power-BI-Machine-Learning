import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.neighbors import KNeighborsClassifier
from tqdm import tqdm
import logging

from src.data_preprocessing import load_raw_data, preprocess_data, save_preprocessed_data
from src.balance_data import balance_dataset, save_balanced_data
from src.model_training import train_and_log_model

logging.basicConfig(level=logging.INFO)

logging.info("Starting churn model training pipeline...")

# Load and preprocess data
df = load_raw_data("data/raw/Customer_Data.csv")
df = preprocess_data(df)
save_preprocessed_data(df, "data/processed/cleaned.csv")

# Ensure target column is int
df['Customer_Status'] = df['Customer_Status'].astype(int)

X = df.drop(columns=['Customer_Status'])
y = df['Customer_Status']

# Split original preprocessed (imbalanced) data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define models
models = {
    "LogisticRegression": LogisticRegression(solver='liblinear'),
    "RandomForest": RandomForestClassifier(n_estimators=100),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss'),
    "LightGBM": LGBMClassifier(),
    "KNN": KNeighborsClassifier()
}

# Train and log on imbalanced dataset
for name in tqdm(models, desc="Training on imbalanced data"):
    train_and_log_model(name, models[name], X_train, y_train, X_test, y_test, dataset_version="v1-cleaned-imbalanced")

# Balance the data
X_bal, y_bal = balance_dataset(X, y)
save_balanced_data(X_bal, y_bal, "data/balanced/balanced.csv")
Xb_train, Xb_test, yb_train, yb_test = train_test_split(X_bal, y_bal, test_size=0.2, random_state=42)

# Train and log on balanced dataset
for name in tqdm(models, desc="Training on balanced data"):
    train_and_log_model(name, models[name], Xb_train, yb_train, Xb_test, yb_test, dataset_version="v1-cleaned-balanced")
