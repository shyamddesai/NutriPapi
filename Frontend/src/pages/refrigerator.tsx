import React, { useState } from 'react';
import styles from '/src/css/refrigerator.module.css';

const MyFridge = () => {
  const [ingredients, setIngredients] = useState<string[]>([]); // Array of ingredients
  const [inputValue, setInputValue] = useState(''); // Current input value

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter' || event.key === ',') {
      event.preventDefault();
      addIngredient(inputValue.trim());
      setInputValue('');
    }
  };

  const addIngredient = (ingredient: string) => {
    if (ingredient && !ingredients.includes(ingredient)) {
      setIngredients([...ingredients, ingredient]);
    }
  };

  const removeIngredient = (ingredientToRemove: string) => {
    setIngredients(ingredients.filter(ingredient => ingredient !== ingredientToRemove));
  };

  const removeAllIngredients = () => {
    setIngredients([]);
  };

  return (
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
        {ingredients.map(ingredient => (
          <li key={ingredient} className={styles.list_item}>
            {ingredient}
            <button onClick={() => removeIngredient(ingredient)}>Remove</button>
          </li>
        ))}
      </ul>
      <button onClick={removeAllIngredients} className={styles.submitButon}>Remove All</button>
    </div>
  );
};

export default MyFridge;

