import axios from 'axios';
import React, { useState, ChangeEvent, FormEvent } from 'react';

const UpdateUserInfoPage = () => {
  const [userInfo, setUserInfo] = useState({
    currentWeight: '',
    targetWeight: '',
    height: '',
    weeklyPhysicalActivity: '',
    gender: '',
    dietaryPreferences: [],
    email: '',
    password: ''
  });
  
  const handleChange = (e: ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    if (name === "dietaryPreferences") {
      // Handle the selection of dietary preferences as an array
      const newPreferences = [...userInfo.dietaryPreferences];
      if (e.target.checked) {
        newPreferences.push(value);
      } else {
        const index = newPreferences.indexOf(value);
        if (index > -1) {
          newPreferences.splice(index, 1);
        }
      }
      setUserInfo({ ...userInfo, dietaryPreferences: newPreferences });
    } else {
      setUserInfo({ ...userInfo, [name]: value });
    }
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const url = 'http://localhost:8000/user/info/';
    
    try {
      const response = await axios.post(url, userInfo, {
        withCredentials: true // Necessary for cookies since session based authentication is used
      });
      console.log(response.data);
      // Handle the successful response
    } catch (error: any) {
      console.error('Error updating user info', error.response?.data || error.message);
    }
  };

  return (
    <div>
      <h1>Update Information</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          name="currentWeight"
          value={userInfo.currentWeight}
          onChange={handleChange}
          placeholder="Current Weight"
        />
        <input
          type="number"
          name="targetWeight"
          value={userInfo.targetWeight}
          onChange={handleChange}
          placeholder="Target Weight"
        />
        <input
          type="number"
          name="height"
          value={userInfo.height}
          onChange={handleChange}
          placeholder="Height"
        />
        <input
          type="number"
          name="weeklyPhysicalActivity"
          value={userInfo.weeklyPhysicalActivity}
          onChange={handleChange}
          placeholder="Weekly Physical Activity"
        />
        <select name="gender" value={userInfo.gender} onChange={handleChange}>
          <option value="">Select Gender</option>
          <option value="M">Male</option>
          <option value="F">Female</option>
          <option value="O">Other</option>
        </select>
        {/* Render checkboxes for dietary preferences */}
        <div>
          {['Vegan', 'Vegetarian', 'Lactose intolerant', 'Nut free', 'Gluten Intolerant', 'Diabetic', 'Kosher', 'Keto'].map(pref => (
            <label key={pref}>
              <input
                type="checkbox"
                name="dietaryPreferences"
                value={pref}
                checked={userInfo.dietaryPreferences.includes(pref)}
                onChange={handleChange}
              />
              {pref}
            </label>
          ))}
        </div>
        <input
          type="email"
          name="email"
          value={userInfo.email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="password"
          name="password"
          value={userInfo.password}
          onChange={handleChange}
          placeholder="Password"
        />
        <button type="submit">Update Information</button>
      </form>
    </div>
  );
};

export default UpdateUserInfoPage;
