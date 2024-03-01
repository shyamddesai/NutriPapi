import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CalorieRecommendationPage = () => {
    const [recommendedCalories, setRecommendedCalories] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchRecommendedCalories = async () => {
            try {
                const response = await axios.get('http://localhost:8000/caloric_recommendation/',{withCredentials:true});
                setRecommendedCalories(response.data.recommended_calories);
            } catch (error) {
                if (error.response) {
                    setError(error.response.data.error || 'An error occurred');
                } else {
                    setError('An error occurred while fetching the data');
                }
            }
        };
        fetchRecommendedCalories();
    }, []);

    return (
        <div>
            <h1>Recommended Caloric Intake</h1>
            {error && <p>Error: {error}</p>}
            {recommendedCalories && (
                <p>Your recommended daily caloric intake is: {recommendedCalories} calories</p>
            )}
        </div>
    );
};

export default CalorieRecommendationPage;
