import React from 'react'
import './loginPage.css'
import { useNavigate } from 'react-router-dom';

const LoginPage = () => {
  
  const navigate = useNavigate(); // Initialize useNavigate

  const handleSignUpClick = () => {
    navigate('/sign-up'); // Navigate to the sign-up page
  };

  return (
    <div className='loginBackground'>
        <section className='login'>
            <h1 className='loginTitle'>Log In</h1>
            <form className='loginForm'>
              <input type="email" placeholder="Email" className="loginInput" />
              <input type="password" placeholder="Password" className="loginInput" />
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