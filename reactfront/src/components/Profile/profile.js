import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './profile.css';

const Profile = () => {
  const [userInfo, setUserInfo] = useState({
    first_name: '',
    gender: '',
    birthday: '',
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
          first_name: data.first_name,
          gender: data.gender,
          birthday: data.birthday,
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
    const url = 'http://localhost:8000/user/update_info/';

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
      <div className='profile'>
        <h1>Update Information</h1>
        <form onSubmit={handleSubmit}>

        <div className="formGroup">
            <label>First Name</label>
            <input type="text" name="first_name" placeholder="First Name" value={userInfo.first_name} onChange={handleChange} required />
          </div>

          <div className="formGroup">
          <label>Gender</label>
            <select name="gender" value={userInfo.gender} onChange={handleChange} required>
              <option value="">Select Gender</option>
              <option value="male">Male</option>
              <option value="female">Female</option>
              <option value="other">Other</option>
            </select>
          </div>

          <div className="formGroup">
            <label>Birthday</label>
            <input type="date" name="birthday" value={userInfo.birthday} onChange={handleChange} required />
          </div>
          
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
            <label>Goals</label>
            <select name="goals" value={userInfo.goals} onChange={handleChange} required>
              <option value="">Select Goals</option>
              <option value="lose">Lose Weight</option>
              <option value="maintain">Maintain Weight</option>
              <option value="gain">Gain Weight</option>
            </select>
          </div>

          <div className="formGroup">
            <label>Weekly Activity Level</label>
            <select name="weekly_physical_activity" value={userInfo.weekly_physical_activity} onChange={handleChange} required>
              <option value="">Select Activity Level</option>
              <option value="1">Sedentary (little or no exercise)</option>
              <option value="2">Lightly active (exercise 1–3 days/week)</option>
              <option value="3">Moderately active (exercise 3–5 days/week)</option>
              <option value="4">Active (exercise 6–7 days/week)</option>
              <option value="5">Very active (hard exercise 6–7 days/week)</option>
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
    </div>
  );
};

export default Profile;
