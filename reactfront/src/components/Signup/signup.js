import React, {useState} from 'react'
import './signup.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SignUp = () => {
  const [credentials, setCredentials] = useState({
    username: '',
    email: '',
    password: '',
  });
  
  const navigate = useNavigate(); // Initialize useNavigate

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to the sign-up page
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setCredentials({ ...credentials, [name]: value });
  };

  const handleSignUpSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/signup/', credentials, { withCredentials: true });
      console.log(response.data);
      localStorage.setItem('userInfo', JSON.stringify(response.data));
      navigate('/signup2'); // Navigate to the next signup step upon successful signup
    } catch (error) {
      console.error('Error during signup:', error.response?.data || error.message);
    }
  };

  return (
    <div className='signupBackground'>
        <section className='signup'>
          <h1 className='signupTitle'>Sign Up</h1>
          <form className='signupForm' onSubmit={handleSignUpSubmit}>
            <input type="username" name="username" placeholder="Username" value={credentials.username} onChange={handleChange} className="signupInput" required/>
            <input type="email" name="email" placeholder="Email" value={credentials.email} onChange={handleChange} className="signupInput" required/>
            <input type="password" name="password" placeholder="Password" value={credentials.password} onChange={handleChange} className="signupInput" required/>
            <button type="submit" className="signupButton">CONTINUE</button>
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