import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [employeeName, setEmployeeName] = useState('');
  const [shiftPreferences, setShiftPreferences] = useState({
    MONDAY: '',
    TUESDAY: '',
    WEDNESDAY: '',
    THURSDAY: '',
    FRIDAY: '',
    SATURDAY: '',
    SUNDAY: ''
  });
  const [schedule, setSchedule] = useState(null);

  // Fetch the initial schedule when the page loads
  useEffect(() => {
    // Call generate_schedule API when the component loads
    const fetchSchedule = async () => {
      try {
        const response = await axios.get('http://localhost:8000/schedule');
        setSchedule(response.data); // Assuming the response contains the schedule data
      } catch (error) {
        console.error("Error fetching the schedule:", error.response || error);
      }
    };

    fetchSchedule(); // Call the function to load the schedule
  }, []);

  // Handle changes to the input fields
  const handleChange = (e) => {
    const { name, value } = e.target;
    setShiftPreferences((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  // Submit form to backend
  const handleSubmit = async (e) => {
    e.preventDefault();

    const employeeData = {
      name: employeeName,
      preferences: shiftPreferences,
    };

    try {
      // Post new employee data
      const response = await axios.post("http://localhost:8000/add_employee", employeeData);      
      // After submitting, refresh the schedule
      const updatedScheduleResponse = await axios.get('http://localhost:8000/schedule');
      setSchedule(updatedScheduleResponse.data); // Assuming the response contains the updated schedule
    } catch (error) {
      if(error.response.data.detail == "Employee could not be added to the schedule, schedule is full"){
        alert("Employee could not be added to the schedule, schedule is full");
      }
      console.error("Error adding employee:", error.response || error);
    }
  };

  return (
    <div className="app-container">
      {/* Left side scheduling form */}
      <div className="form-container">
        <h1>Employee Shift Scheduler</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="employeeName">Employee Name</label>
            <input
              type="text"
              id="employeeName"
              name="employeeName"
              value={employeeName}
              onChange={(e) => setEmployeeName(e.target.value)}
              required
            />
          </div>
          {Object.keys(shiftPreferences).map((day) => (
            <div key={day}>
              <label htmlFor={day}>{day}</label>
              <select
                id={day}
                name={day}
                value={shiftPreferences[day]}
                onChange={handleChange}
                required
              >
                <option value="">Select Shift</option>
                <option value="Morning">Morning</option>
                <option value="Afternoon">Afternoon</option>
                <option value="Evening">Evening</option>
              </select>
            </div>
          ))}
          <button type="submit">Add Employee</button>
        </form>
      </div>

      {/* Right side schedule display */}
      <div className="schedule-container">
        <h2>Schedule</h2>
        {schedule && (
          <table>
            <thead>
              <tr>
                <th>Day</th>
                <th>Morning</th>
                <th>Afternoon</th>
                <th>Evening</th>
              </tr>
            </thead>
            <tbody>
              {Object.keys(schedule).map((day) => (
                <tr key={day}>
                  <td>{day}</td>
                  <td>{schedule[day]?.MORNING?.join(", ") || '-'}</td>
                  <td>{schedule[day]?.AFTERNOON?.join(", ") || '-'}</td>
                  <td>{schedule[day]?.EVENING?.join(", ") || '-'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default App;
