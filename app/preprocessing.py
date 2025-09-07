import pandas as pd
import numpy as np
import re
import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def automate_cleaning_and_feature_engineering_FINAL(df: pd.DataFrame) -> pd.DataFrame:
    """
    Data Cleaning + Feature Engineering for customer dataset.

    Args:
        df: Raw customer data DataFrame

    Returns:
        Cleaned and feature-engineered DataFrame
    """
    try:
        logger.info("🔄 Starting data cleaning and feature engineering...")
        df_copy = df.copy()

        # Drop unnecessary columns
        cols_to_drop = ['ID', 'Customer_ID', 'Month', 'Name', 'SSN']
        df_copy.drop(columns=cols_to_drop, inplace=True, errors='ignore')

        # --- Feature Engineering Helpers ---
        def get_history_months(age_str):
            if pd.isna(age_str):
                return np.nan
            years, months = 0, 0
            y = re.search(r'(\d+)\s+Years', str(age_str))
            m = re.search(r'(\d+)\s+Months', str(age_str))
            if y: years = int(y.group(1))
            if m: months = int(m.group(1))
            return (years * 12) + months

        def count_loans(loan_str):
            if pd.isna(loan_str) or str(loan_str).strip() == '':
                return 0
            return len(str(loan_str).split(','))

        # Credit History Age → Months
        if 'Credit_History_Age' in df_copy.columns:
            df_copy['Credit_History_Months'] = df_copy['Credit_History_Age'].apply(get_history_months)
            df_copy.drop(columns=['Credit_History_Age'], inplace=True, errors='ignore')

        # Loan Type → Number of Loans
        if 'Type_of_Loan' in df_copy.columns:
            df_copy['Num_of_Loan'] = df_copy['Type_of_Loan'].apply(count_loans)
            df_copy.drop(columns=['Type_of_Loan'], inplace=True, errors='ignore')

        # Convert numeric columns - COMPREHENSIVE list including all potentially dirty fields
        numeric_cols = [
            'Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
            'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Delay_from_due_date',
            'Num_of_Delayed_Payment', 'Changed_Credit_Limit', 'Num_Credit_Inquiries',
            'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Total_EMI_per_month',
            'Amount_invested_monthly', 'Monthly_Balance', 'Credit_History_Months'
        ]
        for col in numeric_cols:
            if col in df_copy.columns:
                df_copy[col] = pd.to_numeric(df_copy[col], errors='coerce')

        # Fix impossible negative values
        positive_cols = [
            'Age', 'Num_Bank_Accounts', 'Num_of_Loan', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit'
        ]
        for col in positive_cols:
            if col in df_copy.columns:
                df_copy[col] = df_copy[col].abs()

        # Clean categorical placeholders
        if 'Credit_Mix' in df_copy.columns:
            df_copy['Credit_Mix'] = df_copy['Credit_Mix'].replace('_', np.nan)

        if 'Age' in df_copy.columns:
            df_copy['Age'] = df_copy['Age'].apply(lambda x: x if x <= 100 else np.nan)

        if 'Payment_Behaviour' in df_copy.columns:
            df_copy['Payment_Behaviour'] = df_copy['Payment_Behaviour'].replace('!@9#%8', np.nan)

        # Fill missing values for safe downstream usage
        df_copy = df_copy.fillna(0)

        logger.info("✅ Data cleaning and feature engineering completed")
        return df_copy

    except Exception as e:
        logger.error(f"❌ Error in cleaning and feature engineering: {e}")
        raise
