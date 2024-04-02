import React, { useState } from 'react';
import axios from 'axios';
import './recipes.css';

const Recipes = () => {
    const [importData, setImportData] = useState('');

    const handleImportDataChange = (event) => {
        setImportData(event.target.value);
    };

    const RecipesAndIngredients = async () => {
        try {
            const response = await axios.post(
                'http://localhost:8000/import/',
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

    return (
        <div className="importContainer">
            <h2>Import Recipes and Ingredients</h2>
            <textarea
                value={importData}
                onChange={handleImportDataChange}
                placeholder="Paste JSON data here"
                rows="5"
                className="importTextarea"
            ></textarea>
            <button onClick={RecipesAndIngredients} className="importButton">Import Data</button>
        </div>
    );
};

export default Recipes;