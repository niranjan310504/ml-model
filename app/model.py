import joblib
import pandas as pd
import numpy as np
from .preprocessing import automate_cleaning_and_feature_engineering_FINAL

MODEL_PATH = "models/optimized_credit_model.joblib"
model = joblib.load(MODEL_PATH)

def predict_credit_score(data: dict) -> dict:
    # Convert incoming data to DataFrame
    df = pd.DataFrame([data])
    
    # Apply your comprehensive preprocessing function
    df_processed = automate_cleaning_and_feature_engineering_FINAL(df)
    
    # Get prediction and probabilities
    predicted_category = model.predict(df_processed)[0]
    predicted_proba = model.predict_proba(df_processed)

    # Get class order and map
    class_order = model.classes_  # e.g. ['Good', 'Poor', 'Standard']
    class_map = {name: i for i, name in enumerate(class_order)}

    prob_poor = predicted_proba[:, class_map.get('Poor', 0)][0]
    prob_standard = predicted_proba[:, class_map.get('Standard', 1)][0]
    prob_good = predicted_proba[:, class_map.get('Good', 2)][0]

    # Calculate numerical score using weighted formula
    score = int((prob_poor * 400) + (prob_standard * 650) + (prob_good * 825))

    # Build JSON response
    result = {
        "Customer_ID": data["Customer_ID"],
        "Credit_Score": score,
        "Credit_Category": predicted_category,
        "Lending_Outlook": "Low Risk" if predicted_category == "Good" else "Moderate" if predicted_category == "Standard" else "High Risk",
        "Loan_Type": data.get("Type_of_Loan", "Unknown"),
        "Risk_Factor_1": "High credit inquiries" if data.get("Num_Credit_Inquiries", 0) > 10 else "None",
        "Risk_Factor_2": "Frequent delayed payments" if data.get("Num_of_Delayed_Payment", 0) > 5 else "None",
        "Risk_Factor_3": "High credit utilization" if data.get("Credit_Utilization_Ratio", 0) > 30 else "None",
        "Positive_Factor_1": "Good credit mix" if data.get("Credit_Mix") == "Good" else "None",
        "Positive_Factor_2": "Low outstanding debt" if data.get("Outstanding_Debt", 0) < 1000 else "None",
        "Positive_Factor_3": "Steady income" if data.get("Annual_Income", 0) > 50000 else "None",
        "Improvement_Tip_1": "Reduce inquiries",
        "Improvement_Tip_2": "Pay bills on time",
        "Improvement_Tip_3": "Keep credit utilization below 30%"
    }

    return result

