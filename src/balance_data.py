import pandas as pd
from imblearn.over_sampling import SMOTE
import os
import subprocess

def balance_dataset(X: pd.DataFrame, y: pd.Series):
    smote = SMOTE(random_state=42)
    return smote.fit_resample(X, y)

def save_balanced_data(df: pd.DataFrame, file_path: str):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        df.to_csv(file_path, index=False)
        subprocess.run(["dvc", "add", file_path], check=True)