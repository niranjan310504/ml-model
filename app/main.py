from fastapi import FastAPI
from app.schemas import CreditRequest, CreditResponse
from app.model import predict_credit_score

app = FastAPI(title="Credit Score API")

@app.post("/api", response_model=CreditResponse)
def credit_score_api(request: CreditRequest):
    result = predict_credit_score(request.dict())
    return result
