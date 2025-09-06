from pydantic import BaseModel
from typing import Optional

# Input schema
class CreditRequest(BaseModel):
    ID: str
    Customer_ID: str
    Month: str
    Name: str
    Age: int
    SSN: str
    Occupation: str
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Num_Bank_Accounts: int
    Num_Credit_Card: int
    Interest_Rate: int
    Num_of_Loan: int
    Type_of_Loan: str
    Delay_from_due_date: int
    Num_of_Delayed_Payment: int
    Changed_Credit_Limit: float
    Num_Credit_Inquiries: int
    Credit_Mix: str
    Outstanding_Debt: float
    Credit_Utilization_Ratio: float
    Credit_History_Months: str
    Payment_of_Min_Amount: str
    Total_EMI_per_month: float
    Amount_invested_monthly: float
    Payment_Behaviour: str
    Monthly_Balance: float

# Output schema
class CreditResponse(BaseModel):
    Customer_ID: str
    Credit_Score: int
    Credit_Category: str
    Lending_Outlook: str
    Loan_Type: str
    Risk_Factor_1: str
    Risk_Factor_2: str
    Risk_Factor_3: str
    Positive_Factor_1: str
    Positive_Factor_2: str
    Positive_Factor_3: str
    Improvement_Tip_1: str
    Improvement_Tip_2: str
    Improvement_Tip_3: str
