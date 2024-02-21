import axios from 'axios';
import { useRouter } from 'next/router';
import React, { useState, ChangeEvent, FormEvent } from 'react';

const LoggedInPage = () => {
  const [numCaloriesEatenToday, setNumCaloriesEatenToday] = useState('');
  const router = useRouter();

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    setNumCaloriesEatenToday(e.target.value);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const url = 'http://localhost:8000/api/loggedin/';

    try {
      const response = await axios.post(url, { numCaloriesEatenToday });
      console.log(response.data);
      // Redirect to a new page upon success
      router.push('/dashboard'); // Modify as needed
    } catch (error: unknown) {
      if (error instanceof Error) {
        console.error('Error while submitting calories', error.message);
      } else {
        console.error('An unexpected error occurred', error);
      }
    }
  };

  return (
    <div>
      <h1>Log Your Calories</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="numCaloriesEatenToday"
          value={numCaloriesEatenToday}
          onChange={handleChange}
          placeholder="Number of calories eaten today"
          required
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default LoggedInPage;

