import pandas as pd
import numpy as np
import re

def automate_cleaning_and_feature_engineering_FINAL(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder for your real cleaning logic.
    Copy your actual implementation from the notebook here.
    """
    cols_to_drop = ['ID', 'Customer_ID', 'Month', 'Name', 'SSN']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    def get_history_months(age_str):
        if pd.isna(age_str): return np.nan
        years, months = 0, 0
        y = re.search(r'(\d+)\s+Years', str(age_str)); m = re.search(r'(\d+)\s+Months', str(age_str))
        if y: years = int(y.group(1))
        if m: months = int(m.group(1))
        return (years * 12) + months
    
    def count_loans(loan_str):
        if pd.isna(loan_str) or str(loan_str).strip() == '': return 0
        # This function correctly counts loans and will never be negative.
        return len(str(loan_str).split(','))
    
    df['Credit_History_Months'] = df['Credit_History_Age'].apply(get_history_months)
    df['Num_of_Loan'] = df['Type_of_Loan'].apply(count_loans)
    df.drop(columns=['Credit_History_Age', 'Type_of_Loan'], inplace=True, errors='ignore')
    
    cols_to_convert = [
        'Age', 'Annual_Income', 'Num_of_Loan', 'Num_of_Delayed_Payment', 
        'Changed_Credit_Limit', 'Outstanding_Debt', 
        'Monthly_Balance','Amount_invested_monthly'
    ]
    for col in cols_to_convert:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    cols_for_abs = [
        'Age', 'Num_Bank_Accounts', 'Num_of_Loan', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit'
    ]
    for col in cols_for_abs:
        if col in df.columns:
            df[col] = df[col].abs()
            
    if 'Credit_Mix' in df.columns:
        df['Credit_Mix'].replace('_', np.nan, inplace=True)
        
    if 'Age' in df.columns:
        # Treat any age over 100 as a data error (NaN), to be imputed later
        df['Age'] = df['Age'].apply(lambda x: x if x <= 100 else np.nan)
        
    if 'Payment_Behaviour' in df.columns:
        # Replace the corrupted category with NaN, to be imputed later
        df['Payment_Behaviour'].replace('!@9#%8', np.nan, inplace=True)
    df = df.fillna(0)  # Simplified
    return df

