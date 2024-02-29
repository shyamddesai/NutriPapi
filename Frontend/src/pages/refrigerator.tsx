import React, { useState } from 'react';
import styles from '/src/css/refrigerator.module.css'; // 更新CSS模块的路径
import Image from 'next/image';

// 导入图片
import breakfastImage from 'Frontend/public/assets/Breakfast_001.jpeg';
import lunchImage from 'Frontend/public/assets/Lunch_001.jpeg';
import dinnerImage from 'Frontend/public/assets/Dinner_001.jpg';

const MyFridge = () => {
    const [ingredients, setIngredients] = useState<string[]>([]);
    const [inputValue, setInputValue] = useState<string>('');

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInputValue(event.target.value);
    };

    const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
        if (event.key === 'Enter' || event.key === ',') {
            event.preventDefault();
            if (inputValue.trim() && !ingredients.includes(inputValue.trim())) {
                setIngredients(prevIngredients => [...prevIngredients, inputValue.trim()]);
            }
            setInputValue('');
        }
    };

    const removeIngredient = (ingredientToRemove: string) => {
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
                    <Image src={breakfastImage} alt="Breakfast" width={500} height={300} className={styles.mealImage}/>
                </div>
                <div className={styles.meal}>
                    <h2>Lunch</h2>
                    <Image src={lunchImage} alt="Lunch" width={500} height={300} className={styles.mealImage}/>
                </div>
                <div className={styles.meal}>
                    <h2>Dinner</h2>
                    <Image src={dinnerImage} alt="Dinner" width={500} height={300} className={styles.mealImage}/>
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

export default MyFridge;
