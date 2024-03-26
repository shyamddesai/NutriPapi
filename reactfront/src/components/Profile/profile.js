import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './profile.css';

const Profile = () => {
  const [userInfo, setUserInfo] = useState({
    current_weight: '',
    target_weight: '',
    height: '',
    weekly_physical_activity: '',
    dietary_restriction: '',
  });

  // Set default values for the form fields from the database
  useEffect(() => {
    const fetchUserInfo = async () => {
      const url = 'http://localhost:8000/user/get_info/';
      try {
        const { data } = await axios.get(url, { withCredentials: true });
        console.log(data);
        setUserInfo({
          current_weight: data.current_weight,
          target_weight: data.target_weight,
          height: data.height,
          weekly_physical_activity: data.weekly_physical_activity,
          dietary_restriction: data.dietary_restriction,
        });
      } catch (error) {
        console.error('Failed to fetch user info:', error);
      }
    };

    fetchUserInfo();
  }, []);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setUserInfo({ ...userInfo, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = 'http://localhost:8000/user/info/';

    console.log(userInfo);

    try {
      const response = await axios.post(url, userInfo, {
        withCredentials: true, // Necessary for cookies since session-based authentication is used
      });
      console.log(response.data);
    } catch (error) {
      console.error('Error updating user info', error.response?.data || error.message);
    }
  };

  return (
    <div className="updateUserInfo">
      <h1>Update Information</h1>
      <form onSubmit={handleSubmit}>
        
        <div className="formGroup">
          <label>Current Weight (kgs)</label>
          <input type="range" min="40" max="140" name="current_weight" value={userInfo.current_weight} onChange={handleChange} required />
          <output>{userInfo.current_weight} kgs</output>
        </div>

        <div className="formGroup">
        <label>Target Weight (kgs)</label>
          <input type="range" min="40" max="140" name="target_weight" value={userInfo.target_weight} onChange={handleChange} required />
          <output>{userInfo.target_weight} kgs</output>
        </div>

        <div className="formGroup">
        <label>Height (cm)</label>
          <input type="range" min="120" max="240" name="height" value={userInfo.height} onChange={handleChange} required />
          <output>{userInfo.height} cm</output>
        </div>

        <div className="formGroup">
          <label>Weekly Activity Level</label>
          <select name="weekly_physical_activity" value={userInfo.weekly_physical_activity} onChange={handleChange} required>
            <option value="">Select Activity Level</option>
            <option value="2.5">Sedentary (0-5 hours a week)</option>
            <option value="9">Moderately Active (6-12 hours a week)</option>
            <option value="16">Very Active (12+ hours a week)</option>
          </select>
        </div>

        <div className="formGroup">
          <label>Dietary Preferences</label>
          <select name="dietary_restriction" value={userInfo.dietary_restriction} onChange={handleChange} required>
            <option value="">Select Dietary Preferences</option>
            <option value="none">None</option>
            <option value="lactose">Lactose Intolerant</option>
            <option value="gluten">Gluten-Free</option>
            <option value="vegetarian">Vegetarian</option>
            <option value="vegan">Vegan</option>
            <option value="kosher">Kosher</option>
            <option value="keto">Ketogenic</option>
          </select>
        </div>

        <button className="formSubmitButton" type="submit">Update</button>
      </form>
    </div>
  );
};

export default Profile;
