import React, { useState } from 'react'
import './signup2.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const SignUp2 = () => {
  const [formData, setFormData] = useState({
    first_name: '',
    gender: '',
    goals: '',
    weekly_physical_activity: '',
    birthday: '',
    current_weight: '',
    target_weight: '',
    height: '',
    dietary_restriction: ''
  });

  const navigate = useNavigate();

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/signup_follow/', formData, { withCredentials: true });
      console.log(response.data);
      localStorage.setItem('userInfo', JSON.stringify(response.data));
      navigate('/hub');
    } catch (error) {
      console.error('Error during form submission:', error.response?.data || error.message);
    }

    console.log(formData);
  };

  return (
    <div className='signup2Background'>
      <section className='signup2'>
        <h1 className='signup2Title'>Enter Your Details</h1>
        <form className='signup2Form' onSubmit={handleSubmit}>
          <label className='signup2label'>First Name</label>
          <input type="text" name="first_name" placeholder="First Name" value={formData.first_name} onChange={handleChange} required />

          <label className='signup2label'>Gender</label>
          <select className='signup2select' name="gender" value={formData.gender} onChange={handleChange} required>
            <option value="">Select Gender</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
            <option value="other">Other</option>
          </select>

          <label className='signup2label'>Goals</label>
          <select className='signup2select' name="goals" value={formData.goals} onChange={handleChange} required>
            <option value="">Select Activity Level</option>
            <option value="lose">Lose Weight</option>
            <option value="maintain">Maintain Weight</option>
            <option value="gain">Gain Weight</option>
          </select>

          <label className='signup2label'>Activity Level</label>
          <select className='signup2select' name="weekly_physical_activity" value={formData.weekly_physical_activity} onChange={handleChange} required>
            <option value="">Select Activity Level</option>
            <option value="3">Sedentary (0-5 hours a week)</option>
            <option value="9">Moderately Active (6-12 hours a week)</option>
            <option value="16">Very Active (12+ hours a week)</option>
          </select>

          <label className='signup2label'>Birthday</label>
          <input className='signup2select' type="date" name="birthday" value={formData.birthday} onChange={handleChange} required />

          <label className='signup2label'>Current Weight (kgs)</label>
          <input className='signup2labelslider' type="range" min="40" max="140" name="current_weight" value={formData.current_weight} onChange={handleChange} required />
          <output className='signup2output'>{formData.current_weight} kgs</output>

          <label className='signup2label'>Target Weight (kgs)</label>
          <input className='signup2labelslider' type="range" min="40" max="140" name="target_weight" value={formData.target_weight} onChange={handleChange} required />
          <output className='signup2output'>{formData.target_weight} kgs</output>

          <label className='signup2label'>Height (cm)</label>
          <input className='signup2labelslider' type="range" min="120" max="240" name="height" value={formData.height} onChange={handleChange} required />
          <output className='signup2output'>{formData.height} cm</output>

          <label className='signup2label'>Dietary Preferences</label>
          <select className='signup2select' name="dietary_restriction" value={formData.dietary_restriction} onChange={handleChange} required>
            <option value="">Select Dietary Preferences</option>
            <option value="none">None</option>
            <option value="lactose">Lactose Intolerant</option>
            <option value="gluten">Gluten-Free</option>
            <option value="vegetarian">Vegetarian</option>
            <option value="vegan">Vegan</option>
            <option value="kosher">Kosher</option>
            <option value="keto">Ketogenic</option>
          </select>
          <button type="submit" className="signup2Button">SUBMIT</button>
        </form>
      </section>
    </div>
  );
}

export default SignUp2