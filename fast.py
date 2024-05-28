from fastapi import FastAPI
from pydantic import BaseModel
from paystack import Payment, Status
import secret
class SA(BaseModel):
     ref : str
class User(BaseModel):
    email : str
    cash : float
app = FastAPI()
@app.post("/User/")
def get_user_info(user_input: User):
     email = user_input.email
     cash = user_input.cash
     apple = Payment(secret.secret, email, cash)
     return apple.pay()
@app.post('/ref/')
def ref_id(ref: SA):
     reference = ref.ref
     check = Status(reference, secret.secret)
     return check.verify()