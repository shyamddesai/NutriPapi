import axios from 'axios';
import React from 'react';
import './navbarhub.css';
import logo from '../../../src/assets/iconW.png'
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  const goToHomePage = () => {
    navigate('/');
  }

  const handleSignOut = async () => {
    try {
      await axios.post('http://localhost:8000/signout/', {}, { withCredentials: true });
      console.log('Signed out successfully!');
      navigate('/');
    } catch (error) {
      console.error('Logout failed:', error);
    }
  }

  return (
    <nav className='navbarhubBackground'>
      <div className="navbarhub">
        <div className="desktopMenu">
          <img src={logo} alt="Logo" className='logo' onClick={goToHomePage}/>
        </div>
        <button onClick={handleSignOut} className="navbarSignout">
          Sign Out
        </button>
      </div>      
    </nav>
  );
}

export default Navbar