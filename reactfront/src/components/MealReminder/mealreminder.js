import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './mealreminder.css';

const MealReminder = () => {
  const [reminder, setReminder] = useState('');

  useEffect(() => {
    const checkMealTime = async () => {
      console.log('Checking for meal reminders...');
      try {
        const response = await axios.get('http://localhost:8000/schedule/reminder/', { withCredentials: true });
        if (response.status === 200 && response.data.reminder) {
          setReminder(response.data.reminder);
        }
        console.log('Reminder fetched:', response.data);
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
