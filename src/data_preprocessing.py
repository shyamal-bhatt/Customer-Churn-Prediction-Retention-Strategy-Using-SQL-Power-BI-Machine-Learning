import pandas as pd
import os
import subprocess
import logging
import pyodbc
from sklearn.preprocessing import LabelEncoder

logging.basicConfig(level=logging.INFO)

def get_sql_connection():
    try:
        conn = pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=MRSTOCK\HUMBER_DB;'
            r'DATABASE=db_Churn;'
            r'Trusted_Connection=yes;'
        )
        return conn
    except pyodbc.OperationalError as e:
        logging.error(f"SQL connection failed: {e}")
        raise

def load_or_fetch_view(view_name: str, file_path: str) -> pd.DataFrame:
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    conn = get_sql_connection()
    df = pd.read_sql(f"SELECT * FROM {view_name}", conn)
    conn.close()
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    subprocess.run(["dvc","add",file_path], check=True)
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    drop_cols = ['Customer_ID','Churn_Category','Churn_Reason']
    data.drop(columns=[c for c in drop_cols if c in data.columns], axis = 1, inplace=True)
    columns_to_encode = [
        'Gender','Married','State','Value_Deal','Phone_Service','Multiple_Lines',
        'Internet_Service','Internet_Type','Online_Security','Online_Backup',
        'Device_Protection_Plan','Premium_Support','Streaming_TV','Streaming_Movies',
        'Streaming_Music','Unlimited_Data','Contract','Paperless_Billing','Payment_Method'
    ]
    for col in columns_to_encode:
        if col in data.columns:
            data[col] = LabelEncoder().fit_transform(data[col].astype(str))
    if 'Customer_Status' in data.columns:
        data['Customer_Status'] = data['Customer_Status'].map({'Stayed':0,'Churned':1})
    return data