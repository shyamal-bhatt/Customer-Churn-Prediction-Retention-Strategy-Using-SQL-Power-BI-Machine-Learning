from sklearn.metrics import classification_report
from typing import Union
import logging

logging.basicConfig(level=logging.INFO)

def print_classification_metrics(y_true, y_pred) -> None:
    logging.info("Generating classification report...")
    report = classification_report(y_true, y_pred)
    print("\nClassification Report:\n")
    print(report)