import React, { useState } from 'react';
import './loginPage.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    password: '',
  });

  const navigate = useNavigate(); // Initialize useNavigate

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCredentials(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/signin/', credentials, { withCredentials: true });
      console.log(response.data);
      localStorage.setItem('userInfo', JSON.stringify(response.data));
      navigate('/hub');
    } catch (error) {
      console.error('Error during login:', error.response?.data || error.message);
    }
  };

  const handleSignUpClick = () => {
    navigate('/signup');
  };

  return (
    <div className='loginBackground'>
        <section className='login'>
            <h1 className='loginTitle'>Log In</h1>
            <form className='loginForm' onSubmit={handleLogin}>
              <input type="username" name="username" placeholder="Username" value={credentials.username} onChange={handleChange} className="loginInput" required/>
              <input type="password" name="password" placeholder="Password" value={credentials.password} onChange={handleChange} className="loginInput" required/>
              <button type="submit" className="loginButton">LOG IN</button>
            </form>
            <div className='loginForm2'>
              <h4 className='loginToSignUp'>
                Don’t have an account? <span className="signUpLink" onClick={handleSignUpClick}>Create an Account</span>
              </h4>
            </div>
        </section>
    </div>
  );
}

export default LoginPage