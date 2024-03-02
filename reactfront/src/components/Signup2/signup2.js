import React from 'react'
import './signup2.css'
import { useNavigate } from 'react-router-dom';

const SignUp2 = () => {
  
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to the sign-up page
  };

  const handleSignUpContClick = () => {
    navigate('/sign-up2'); // Navigate to the sign-up page
  };

  return (
    <div className='signup2Background'>
        <section className='signup2'>
          <h1 className='signup2Title'>Sign Up</h1>
          <form className='signup2Form'>
            <input type="firstname" placeholder="First name" className="signup2Input" />
            <input type="lastname" placeholder="Last name" className="signup2Input" />
            <input type="email" placeholder="Email" className="signup2Input" />
            <input type="password" placeholder="Password" className="signup2Input" />
            <button type="submit" className="signupButton" onClick={handleSignUpContClick}>CONTINUE</button>
          </form>
          <div className='signup2Form2'>
              <h4 className='signup2ToLogIn'>
                Already have an account? <span className="login2Link" onClick={handleLoginClick}>Log In</span>
              </h4>
            </div>
        </section>
    </div>
  );
}

export default SignUp2