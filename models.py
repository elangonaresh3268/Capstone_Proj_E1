from pydantic import BaseModel

class UserProfile(BaseModel):
    name:str
    age:int
    gender:str
    occupation:str
    income:float
    marital_status:str
    medical_history:str
    existing_policy:str


class Recommendation(BaseModel):
    policy_name:str