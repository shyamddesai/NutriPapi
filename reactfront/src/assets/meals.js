import React, { useState } from 'react';
import styles from './meals.css';
import breakfastImage from './assets/Breakfast_001.jpeg';
import lunchImage from './assets/Lunch_001.jpeg';
import dinnerImage from './assets/Dinner_001.jpg';

const Meals = () => {
    const [ingredients, setIngredients] = useState([]);
    const [inputValue, setInputValue] = useState('');

    const handleInputChange = (event) => {
        setInputValue(event.target.value);
    };

    const handleKeyPress = (event) => {
        if (event.key === 'Enter' || event.key === ',') {
            event.preventDefault();
            if (inputValue.trim() && !ingredients.includes(inputValue.trim())) {
                setIngredients(prevIngredients => [...prevIngredients, inputValue.trim()]);
            }
            setInputValue('');
        }
    };

    const removeIngredient = (ingredientToRemove) => {
        setIngredients(prevIngredients => prevIngredients.filter(ingredient => ingredient !== ingredientToRemove));
    };

    const removeAllIngredients = () => {
        setIngredients([]);
    };

    return (
        <div>
            <div className={styles.mealsContainer}>
                <div className={styles.meal}>
                    <h2>Breakfast</h2>
                    <img src={breakfastImage} alt="Breakfast" width={500} height={300} className={styles.mealImage}/>
                </div>
                <div className={styles.meal}>
                    <h2>Lunch</h2>
                    <img src={lunchImage} alt="Lunch" width={500} height={300} className={styles.mealImage}/>
                </div>
                <div className={styles.meal}>
                    <h2>Dinner</h2>
                    <img src={dinnerImage} alt="Dinner" width={500} height={300} className={styles.mealImage}/>
                </div>
            </div>
            <div className={styles.fridgeContainer}>
                <label htmlFor="fridgeInput">My Fridge</label>
                <p>Press enter or add a comma after each ingredient</p>
                <input
                    id="fridgeInput"
                    type="text"
                    value={inputValue}
                    onChange={handleInputChange}
                    onKeyPress={handleKeyPress}
                    placeholder="Add ingredients"
                />
                <ul className={styles.list}>
                    {ingredients.map((ingredient, index) => (
                        <li key={index} className={styles.list_item}>
                            {ingredient}
                            <button onClick={() => removeIngredient(ingredient)}>Remove</button>
                        </li>
                    ))}
                </ul>
                <button onClick={removeAllIngredients} className={styles.submitButton}>Remove All</button>
            </div>
        </div>
    );
};

export default Meals;
