import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './mealReminder.module.css';

const MealReminder = () => {
  const [reminder, setReminder] = useState('');

  useEffect(() => {
    const checkMealTime = async () => {
      try {
        const response = await axios.get('http://localhost:8000/reminder/', { withCredentials: true });
        if (response.status === 200) {
          setReminder(response.data.reminder);
        }
      } catch (error) {
        console.error('Error fetching meal reminder:', error);
      }
    };

    const interval = setInterval(checkMealTime, 60000); // Check every minute
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      {reminder && (
        <div className="reminderNotification">
          {reminder}
        </div>
      )}
    </div>
  );
};

export default MealReminder;
