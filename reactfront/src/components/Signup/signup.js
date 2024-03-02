import React from 'react'
import './signup.css'
import { useNavigate } from 'react-router-dom';

const SignUp = () => {
  
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to the sign-up page
  };

  const handleSignUpContClick = () => {
    navigate('/sign-up2'); // Navigate to the sign-up page
  };

  return (
    <div className='signupBackground'>
        <section className='signup'>
          <h1 className='signupTitle'>Sign Up</h1>
          <form className='signupForm'>
            <input type="firstname" placeholder="First name" className="signupInput" required/>
            <input type="lastname" placeholder="Last name" className="signupInput" required/>
            <input type="email" placeholder="Email" className="signupInput" required/>
            <input type="password" placeholder="Password" className="signupInput" required/>
            <button type="submit" className="signupButton" onClick={handleSignUpContClick}>CONTINUE</button>
          </form>
          <div className='signupForm2'>
              <h4 className='signupToLogIn'>
                Already have an account? <span className="loginLink" onClick={handleLoginClick}>Log In</span>
              </h4>
            </div>
        </section>
    </div>
  );
}

export default SignUp