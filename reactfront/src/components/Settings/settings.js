import axios from 'axios';
import React, { useState, useEffect } from 'react';
import './settings.css';

const Settings = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    email: '',
    new_password: '',
  });

  useEffect(() => {
    const fetchUserInfo = async () => {
      const url = 'http://localhost:8000/user/get_info/';
      try {
        const { data } = await axios.get(url, { withCredentials: true });
        console.log(data);
        setUserInfo({
          ...userInfo,
          username: data.username,
          email: data.email,
        });
      } catch (error) {
        console.error('Failed to fetch user info:', error);
      }
    };

    fetchUserInfo();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const url = 'http://localhost:8000/user/change_password/';
    try {
      const response = await axios.post(url, { new_password: userInfo.new_password }, { withCredentials: true });
      console.log(response.data);
      // Handle success here, e.g., showing a success message
    } catch (error) {
      console.error('Error updating password:', error.response?.data || error.message);
      // Handle error here, e.g., showing an error message
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setUserInfo(prev => ({ ...prev, [name]: value }));
  };

  return (
    <div className="updateSettings">
      <h1>Account Settings</h1>
      <div className="userInfoDisplay">
        <p><strong>Username: </strong> {userInfo.username}</p>
        <p><strong>Email: </strong> {userInfo.email}</p>
      </div>

      <h2>Change Password</h2>
      <form onSubmit={handleSubmit}>
        <div className="formGroup">
          <label>Change Password</label>
          <input
            type="password"
            name="new_password"
            placeholder="Enter new password"
            value={userInfo.new_password}
            onChange={handleChange}
            required
          />
        </div>
        <button className="formSubmitButton" type="submit">Update Password</button>
      </form>
    </div>
  );
};

export default Settings;
