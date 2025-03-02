from pydantic import BaseModel

class EmployeePayload(BaseModel):
    name: str
    preferences: dict[str, str]
    