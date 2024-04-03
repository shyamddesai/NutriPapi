import axios from 'axios';
import React, { useState } from 'react';
import './meals.css';
import MealReminder from '../MealReminder/mealreminder';
import breakfastImage from '../../assets/Breakfast_001.jpeg';
import lunchImage from '../../assets/Lunch_001.jpeg';
import dinnerImage from '../../assets/Dinner_001.jpg';

const Meals = () => {
    const [ingredients, setIngredients] = useState([]);
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter' || event.key === ',') {
            event.preventDefault();
            const newIngredient = inputValue.trim();
            if (newIngredient && !ingredients.includes(newIngredient)) {
                addIngredient(newIngredient);
            }
            setInputValue('');
        }
    };

    const addIngredient = async (ingredient) => {
        try {
            await axios.post(
                'http://localhost:8000/fridge/add_ingredient/',
                { ingredients: [ingredient] },
                { withCredentials: true }
            );
            console.log('Added ingredient:', ingredient);
            setIngredients(prevIngredients => [...prevIngredients, ingredient]);
        } catch (error) {
            console.error('Failed to add ingredient:', error);
        }
    };

    const removeIngredient = async (ingredientToRemove) => {
        try {
            await axios.post(
                'http://localhost:8000/fridge/remove_ingredient/',
                { ingredient: ingredientToRemove },
                { withCredentials: true }
            );
            console.log('Removed ingredient:', ingredientToRemove);
            setIngredients(prevIngredients => prevIngredients.filter(ingredient => ingredient !== ingredientToRemove));
        } catch (error) {
            console.error('Failed to remove ingredient:', error);
        }
    };

    const removeAllIngredients = async () => {
        try {
            await axios.post(
                'http://localhost:8000/fridge/remove_ingredient/',
                { ingredients: [] },
                { withCredentials: true }
            );
            setIngredients([]);
        } catch (error) {
            console.error('Failed to clear ingredients:', error);
        }
    };

    return (
        <div>
            <div>
                <MealReminder />
            </div>

            <div className="mealsContainer">
                <div className="meal">
                    <h2>Breakfast</h2>
                    <img src={breakfastImage} alt="Breakfast" width={500} height={300} className="mealImage" />
                </div>
                <div className="meal">
                    <h2>Lunch</h2>
                    <img src={lunchImage} alt="Lunch" width={500} height={300} className="mealImage" />
                </div>
                <div className="meal">
                    <h2>Dinner</h2>
                    <img src={dinnerImage} alt="Dinner" width={500} height={300} className="mealImage" />
                </div>
            </div>
            <div className="fridgeContainer">
                <label htmlFor="fridgeInput" className="fridgeInputLabel">My Fridge</label>
                <p>Press enter or add a comma after each ingredient</p>
                <input
                    id="fridgeInput"
                    type="text"
                    value={inputValue}
                    onChange={handleInputChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Add ingredients"
                    className="fridgeInput"
                />
                <ul className="list">
                    {ingredients.map((ingredient, index) => (
                        <li key={index} className="listItem">
                            {ingredient}
                            <button onClick={() => removeIngredient(ingredient)} className="listItemButton">Remove</button>
                        </li>
                    ))}
                </ul>
                <button onClick={removeAllIngredients} className="submitButton">Remove All</button>
            </div>
        </div>
    );
};

export default Meals;
