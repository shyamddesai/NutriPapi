import React, { useState } from 'react';
import axios from 'axios';
import './recipes.css';

const Recipes = () => {
    const [importData, setImportData] = useState('');
    const [scheduledDate, setScheduledDate] = useState('');

    const handleImportDataChange = (event) => {
        setImportData(event.target.value);
    };

    const handleScheduledDateChange = (event) => {
        setScheduledDate(event.target.value);
    };

    const importRecipesAndIngredients = async () => {
        try {
            const response = await axios.post(
                'http://localhost:8000/recipe/add/',
                { data: importData },
                { headers: { 'Content-Type': 'application/json' }, withCredentials: true }
            );
            console.log('Import successful', response.data);
            alert('Recipes and ingredients imported successfully!');
            setImportData('');
        } catch (error) {
            console.error('Failed to import data:', error);
            alert('Failed to import recipes and ingredients.');
        }
    };

    const scheduleMeal = async () => {
        try {
            const response = await axios.post(
                'http://localhost:8000/schedule/add',
                { date: scheduledDate },
                { withCredentials: true }
            );
            console.log('Meal scheduled successfully', response.data);
            alert(`Meal scheduled successfully for ${scheduledDate}.`);
        } catch (error) {
            console.error('Failed to schedule meal:', error);
            alert('Failed to schedule meal.');
        }
    };

    return (
        <div>
            <div className="importContainer">
                <h2>Import Recipes and Ingredients</h2>
                <textarea
                    value={importData}
                    onChange={handleImportDataChange}
                    placeholder="Paste JSON data here"
                    rows="5"
                    className="importTextarea"
                ></textarea>
                <button onClick={importRecipesAndIngredients} className="importButton">Import Data</button>
            </div>
            <div className="scheduleMealContainer">
                <h2>Schedule Meal</h2>
                <input
                    type="date"
                    value={scheduledDate}
                    onChange={handleScheduledDateChange}
                    className="scheduleInput"
                />
                {/* <select
                    value={mealType}
                    onChange={handleMealTypeChange}
                    className="mealTypeSelect"
                >
                    <option value="breakfast">Breakfast</option>
                    <option value="lunch">Lunch</option>
                    <option value="dinner">Dinner</option>
                </select> */}
                <button onClick={scheduleMeal} className="scheduleButton">Schedule Meal</button>
            </div>
        </div>
    );
};

export default Recipes;