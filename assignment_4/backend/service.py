from fastapi import HTTPException
import json
from backend.constants import (
    MAX_DAYS_PER_EMPLOYEE,
    SHIFT_TYPES,
)

SCHEDULE_FILE = "backend/schedule.json"


class Employee:
    def __init__(self, name, preferences):
        self.name = name
        self.shifts = []
        self.preferences = preferences


class Schedule:
    def __init__(self):
        self.schedule = {
            "MONDAY": {},
            "TUESDAY": {},
            "WEDNESDAY": {},
            "THURSDAY": {},
            "FRIDAY": {},
            "SATURDAY": {},
            "SUNDAY": {},
        }
        with open(SCHEDULE_FILE, "r") as file:
            schedule_json = json.load(file)
            if schedule_json:
                self.schedule = schedule_json

    def add_shift_to_schedule(
        self, day, time, employee: Employee, leftover_preferences
    ):
        for shift in SHIFT_TYPES:
            if employee.name in self.schedule[day].get(shift, []):
                leftover_preferences[day] = time
                return employee, leftover_preferences
        if day not in self.schedule:
            self.schedule[day] = {time.upper(): [employee.name]}
            employee.shifts.append((day, time.upper()))
        elif day in self.schedule and time.upper() not in self.schedule[day]:
            self.schedule[day][time.upper()] = [employee.name]
            employee.shifts.append((day, time.upper()))
        elif (
            day in self.schedule
            and time.upper() in self.schedule[day]
            and len(self.schedule[day][time.upper()]) < 2
        ):
            self.schedule[day][time.upper()].append(employee.name)
            employee.shifts.append((day, time.upper()))
        elif (
            day in self.schedule
            and time.upper() in self.schedule[day]
            and len(self.schedule[day][time.upper()]) >= 2
        ):
            leftover_preferences[day] = time.upper()
        return employee, leftover_preferences

    def add_new_employee_shifts(self, employee: Employee):
        leftover_preferences = {}
        # preferences aware scheduling
        for day, time in employee.preferences.items():
            employee, leftover_preferences = self.add_shift_to_schedule(
                day, time, employee, leftover_preferences
            )
        # day aware scheduling
        if leftover_preferences and len(employee.shifts) < MAX_DAYS_PER_EMPLOYEE:
            for day, time in leftover_preferences.items():
                for aval_time in SHIFT_TYPES:
                    employee, leftover_preferences = self.add_shift_to_schedule(
                        day, aval_time, employee, leftover_preferences
                    )
        # no day no time aware scheduling
        for day in self.schedule:
            for time in SHIFT_TYPES:
                if (
                    len(employee.shifts) < MAX_DAYS_PER_EMPLOYEE
                    and (day, time) not in employee.shifts
                    and len(self.schedule[day].get(time, [])) < 2
                ):
                    employee, leftover_preferences = self.add_shift_to_schedule(
                        day, time, employee, leftover_preferences
                    )

        if len(employee.shifts) == 0:
            raise HTTPException(
                status_code=400,
                detail="Employee could not be added to the schedule, schedule is full",
            )
        return employee


def add_employee(name: str, preferences: dict[str, str]):
    employee = Employee(name, preferences)
    schedule = Schedule()
    employee = schedule.add_new_employee_shifts(employee)
    with open(SCHEDULE_FILE, "w") as file:
        json.dump(schedule.schedule, file)
    return schedule.schedule


def generate_schedule():
    with open(SCHEDULE_FILE, "r") as file:
        schedule_json = json.load(file)
    return schedule_json
