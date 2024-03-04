import React, {useState} from 'react'
import './signup2.css'
import { useNavigate } from 'react-router-dom';

const SignUp2 = () => {
  
  const navigate = useNavigate(); // Initialize useNavigate
  const [gender, setGender] = useState(''); 
  const [goals, setGoals] = useState('');
  const [activityLevel, setActivityLevel] = useState('');
  const [birthday, setBirthday] = useState('');
  const [currentWeight, setCurrentWeight] = useState('');
  const [targetWeight, setTargetWeight] = useState('');
  const [height, setHeight] = useState('');
  const [dietaryPreferences, setDietaryPreferences] = useState('');
  
  const handleSubmit = (event) => {
    event.preventDefault();
    // Here you would typically handle the form submission, e.g., sending data to a backend server
    // For demonstration, we'll just navigate to a different route
    navigate('/hub'); // Adjust the navigation target as needed
};
  return (
    <div className='signup2Background'>
        <section className='signup2'>
          <h1 className='signup2Title'>Enter Your Details</h1>
          <form className='signup2Form' onSubmit={handleSubmit}>
            <label className='signup2label'>Gender</label>
                <select className='signup2select' value={gender} onChange={(e) => setGender(e.target.value)} required>
                    <option value="">Select Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
              <label className='signup2label'>Goals</label>
                <select className='signup2select' value={goals} onChange={(e) => setGoals(e.target.value)} required>
                      <option value="">Select Activity Level</option>
                      <option value="lose">Lose Weight</option>
                      <option value="maintain">Maintain Weight</option>
                      <option value="gain">Gain Weight</option>
                </select>
              <label className='signup2label'>Activity Level</label>
                <select className='signup2select' value={activityLevel} onChange={(e) => setActivityLevel(e.target.value)} required>
                    <option value="">Select Activity Level</option>
                    <option value="low">Low</option>
                    <option value="medium">Medium</option>
                    <option value="high">High</option>
                </select>
              <label className='signup2label'>Birthday</label>
                <input className='signup2select' type="date" value={birthday} onChange={(e) => setBirthday(e.target.value)} required />
              <label className= 'signup2label'>Current Weight (kgs)</label>
                <input className = 'signup2labelslider' type="range" min="40" max="140" value={currentWeight} onChange={(e) => setCurrentWeight(e.target.value)} required />
                <output className='signup2output'>{currentWeight} kgs</output>
              <label className='signup2label'>Target Weight (kgs)</label>
                <input className = 'signup2labelslider' type="range" min="40" max="140" value={targetWeight} onChange={(e) => setTargetWeight(e.target.value)} required />
                <output className='signup2output'>{targetWeight} kgs</output>
              <label className='signup2label'>Height (cm)</label>
                <input className = 'signup2labelslider' type="range" min="120" max="240" value={height} onChange={(e) => setHeight(e.target.value)} required />
                <output className='signup2output'>{height} cm</output>

              <label className='signup2label'>Dietary Preferences</label>
                <select className='signup2select' value={dietaryPreferences} onChange={(e) => setDietaryPreferences(e.target.value)} required>
                    <option value="">Select Dietary Preferences</option>
                    <option value="none">None</option>
                    <option value="pescatarian">Pescatarian</option>
                    <option value="vegetarian">Vegetarian</option>
                    <option value="lactose">Lactose Intolerant</option>
                    <option value="vegan">Vegan</option>
                </select>
              <button type="submit" className="signup2Button">SUBMIT</button>
          </form>
        </section>
    </div>
  );
}

export default SignUp2