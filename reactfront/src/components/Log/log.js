import axios from 'axios';
import React, { useState } from 'react';
import './log.css';

const Log = () => {
    const [mealLog, setMealLog] = useState({
        breakfast: '',
        lunch: '',
        dinner: '',
        exercise: '',
    });
    const [showSuccess, setShowSuccess] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setMealLog({ ...mealLog, [name]: value });
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

    return (
        <div className="logContainer">
            <div className="card">
                <h1 className="title">Daily Log</h1>
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
                            required
                        />
                    </div>
                    <button type="submit" className="submitButton">Submit</button>
                </form>
            </div>

            {showSuccess && (
                <div className="successNotification">
                    Log submitted successfully!
                </div>
            )}
        </div>
    );
};

export default Log;
