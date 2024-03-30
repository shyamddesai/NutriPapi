import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './log.css';

const Log = () => {
    const [mealLog, setMealLog] = useState({
        breakfast: 0,
        lunch: 0,
        dinner: 0,
        snacks: 0,
    });
    const [showSuccess, setShowSuccess] = useState(false);

    useEffect(() => {
        const fetchMealLogs = async () => {
            try {
                const response = await axios.get('http://localhost:8000/meals/view_log/', { withCredentials: true });
                const mealLogs = response.data.meal_logs;
                if (mealLogs.length !== 0) {
                    const { breakfast, lunch, dinner, snacks } = mealLogs[0];
                    setMealLog({ breakfast: breakfast, lunch: lunch, dinner: dinner, snacks: snacks });
                }
            } catch (error) {
                console.error('Error fetching meal logs:', error);
            }
        };

        fetchMealLogs();
    }, []);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setMealLog({
            ...mealLog,
            [name]: value === '' ? 0 : isNaN(value) ? mealLog[name] : parseInt(value),
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const url = 'http://localhost:8000/meals/log/';
        try {
            const response = await axios.post(url, mealLog, { withCredentials: true });
            console.log(response.data);
            setShowSuccess(true);
            setTimeout(() => setShowSuccess(false), 3000);
        } catch (error) {
            if (axios.isAxiosError(error) && error.response) {
                console.error('Error response', error.response.data);
            } else if (error instanceof Error) {
                console.error('Error message', error.message);
            } else {
                console.error('Unexpected error', error);
            }
        }
    };

    // Get today's date in YYYY-MM-DD format
    const today = new Date().toISOString().slice(0, 10);

    return (
        <div className="logContainer">
            <div className="card">
                <h1 className="title">Daily Calories Log</h1>
                <h3 className="logDate">Date: {today}</h3>
                <form onSubmit={handleSubmit} className="form">
                    <div className="inputGroup">
                        <label htmlFor="breakfast" className="label">Breakfast</label>
                        <input
                            type="text"
                            id="breakfast"
                            name="breakfast"
                            value={mealLog.breakfast}
                            onChange={handleChange}
                            className="inputField"
                            placeholder="Enter breakfast calories"
                            required
                        />
                    </div>
                    <div className="inputGroup">
                        <label htmlFor="lunch" className="label">Lunch</label>
                        <input
                            type="text"
                            id="lunch"
                            name="lunch"
                            value={mealLog.lunch}
                            onChange={handleChange}
                            className="inputField"
                            placeholder="Enter lunch calories"
                            required
                        />
                    </div>
                    <div className="inputGroup">
                        <label htmlFor="dinner" className="label">Dinner</label>
                        <input
                            type="text"
                            id="dinner"
                            name="dinner"
                            value={mealLog.dinner}
                            onChange={handleChange}
                            className="inputField"
                            placeholder="Enter dinner calories"
                            required
                        />
                    </div>
                    <div className="inputGroup">
                        <label htmlFor="snacks" className="label">Snacks</label>
                        <input
                            type="text"
                            id="snacks"
                            name="snacks"
                            value={mealLog.snacks}
                            onChange={handleChange}
                            className="inputField"
                            placeholder="Enter snacks calories"
                            required
                        />
                    </div>
                    <button type="submit" className="submitButton">Submit</button>
                </form>
            </div>

            {showSuccess && (
                <div className="successNotification">
                    Log successfully submitted for today!
                </div>
            )}
        </div>
    );
};

export default Log;
