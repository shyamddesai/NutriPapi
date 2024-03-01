import React from 'react';
import './navbar.css';
import logo from '../../../src/assets/iconW.png'
import { Link } from 'react-scroll'; //npmjs package
import { useNavigate } from 'react-router-dom';


const Navbar = () => {

  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login'); // Navigate to the login page
  };

  const goToHomePage = () => {
    navigate('/');
  }

  return (
    <nav className='navbarBackground'>
      <div className="navbar">
        <div className="desktopMenu">
          <img src={logo} alt="Logo" className='logo' onClick={goToHomePage}/>
          <div className="dektopMenuTabs">
            <a href="/hub" className="desktopMenuListItem">Hub</a>              
            <Link to="about" spy={true} smooth={true} offset={-200} duration={500} className="desktopMenuListItem">About Us</Link>
            <Link to="testi" spy={true} smooth={true} offset={-200} duration={500} className="desktopMenuListItem">Testimonials</Link>
          </div>
        </div>
        <button className="desktopMenuBtn" onClick={handleLoginClick}>
          Log In
        </button>
      </div>      
    </nav>
  );
}


export default Navbar