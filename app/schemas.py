from pydantic import BaseModel
from typing import Optional, Union

# Input schema - accepts raw/dirty data that needs preprocessing
class CreditRequest(BaseModel):
    ID: str
    Customer_ID: str
    Month: str
    Name: str
    Age: Union[str, int, float]  # Can be dirty like "25_" 
    SSN: str
    Occupation: str
    Annual_Income: Union[str, int, float]  # Can be dirty
    Monthly_Inhand_Salary: Union[str, int, float]  # Can be dirty
    Num_Bank_Accounts: Union[str, int, float]  # Can be dirty
    Num_Credit_Card: Union[str, int, float]  # Can be dirty
    Interest_Rate: Union[str, int, float]  # Can be dirty
    Num_of_Loan: Union[str, int, float]  # Can be dirty like "7_"
    Type_of_Loan: str
    Delay_from_due_date: Union[str, int, float]  # Can be dirty
    Num_of_Delayed_Payment: Union[str, int, float]  # Can be dirty
    Changed_Credit_Limit: Union[str, int, float]  # Can be dirty
    Num_Credit_Inquiries: Union[str, int, float]  # Can be dirty like "2022.0"
    Credit_Mix: str
    Outstanding_Debt: Union[str, int, float]  # Can be dirty
    Credit_Utilization_Ratio: Union[str, int, float]  # Can be dirty
    Credit_History_Age: str  # Will be converted to Credit_History_Months
    Payment_of_Min_Amount: str
    Total_EMI_per_month: Union[str, int, float]  # Can be dirty
    Amount_invested_monthly: Union[str, int, float]  # Can be dirty
    Payment_Behaviour: str
    Monthly_Balance: Union[str, int, float]  # Can be dirty

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
