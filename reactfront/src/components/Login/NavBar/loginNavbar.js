import React from 'react';
import './loginNavbar.css';
import logo from '../../../../src/assets/iconW.png'
import { Link } from 'react-scroll'; //npmjs package
import { useNavigate } from 'react-router-dom';


const Navbar = () => {

  const navigate = useNavigate();

  const goToHomePage = () => {
    navigate('/');
  }

  return (
    <nav className='navbarBackground'>
      <div className="navbar">
        <div className="desktopMenu">
          <img src={logo} alt="Logo" className='logo' onClick={goToHomePage}/>
          <div className="dektopMenuTabs">
          </div>
        </div>
      </div>      
    </nav>
  );
}


export default Navbar