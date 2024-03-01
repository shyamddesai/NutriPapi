import React, { useState } from 'react';
import axios from 'axios';

const CaloriePage = () => {
    const [calories, setCalories] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [submitted, setSubmitted] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        setSubmitted(false);

        try {
            const response = await axios.post('http://localhost:8000/loggedin/', {
                caloriesConsumed: calories

            },
                {withCredentials: true});
            setCalories(response.data.caloriesConsumed);
            setSubmitted(true);
        } catch (error) {
            if (error.response) {
                setError(error.response.data.error || 'An error occurred');
            } else {
                setError('An error occurred while fetching the data');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h1>Calorie</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Calories Consumed:
                    <input
                        type="text"
                        value={calories}
                        onChange={(e) => setCalories(e.target.value)}
                        disabled={loading}
                    />
                </label>
                <button type="submit" disabled={loading}>Submit</button>
            </form>
            {error && <p>Error: {error}</p>}
            {!error && submitted && <p>Calories Consumed: {calories}</p>}
        </div>
    );
};

export default CaloriePage;
