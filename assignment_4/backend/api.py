from backend.service import add_employee, generate_schedule
import uvicorn
from backend.models import EmployeePayload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post("/add_employee")
async def add_employee_route(employee: EmployeePayload):
    new_schedule = add_employee(employee.name, employee.preferences)
    return new_schedule

@app.get("/schedule")
async def schedule_shifts():
    schedule = generate_schedule()
    return schedule

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)