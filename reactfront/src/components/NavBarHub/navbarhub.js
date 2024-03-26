import React from 'react';
import './navbarhub.css';
import logo from '../../../src/assets/iconW.png'
import { Link } from 'react-scroll'; //npmjs package
import { useNavigate } from 'react-router-dom';


const Navbar = () => {

  const navigate = useNavigate();

  const goToHomePage = () => {
    navigate('/');
  }

  return (
    <nav className='navbarhubBackground'>
      <div className="navbarhub">
        <div className="desktopMenu">
          <img src={logo} alt="Logo" className='logo' onClick={goToHomePage}/>
        </div>
        <button className="navbarSignout">
          Sign Out
        </button>
      </div>      
    </nav>
  );
}


export default Navbar