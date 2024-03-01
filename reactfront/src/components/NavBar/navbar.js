import React from 'react';
import './navbar.css';
import logo from '../../../src/assets/iconW.png'
import { Link } from 'react-scroll'; //npmjs package
import { Router, useNavigate } from 'react-router-dom';

const Navbar = () => {
  // const history = useNavigate();
  // const handleLogin = () => {
  //   // Redirect to the login page
  //   history.push('/login');
  // };


  return (
    <nav className='navbarBackground'>
        <div className="navbar">
            <div className="desktopMenu">
            <img src={logo} alt="Logo" className='logo'/>
              <div className="dektopMenuTabs">
                <a href="/hub" className="desktopMenuListItem">Hub</a>              
                <Link to="about" spy={true} smooth={true} offset={50} duration={500} className="desktopMenuListItem">About</Link>
                <Link to="products" spy={true} smooth={true} offset={50} duration={500} className="desktopMenuListItem">Testimonial</Link>
              </div>
              </div>
            <button className="desktopMenuBtn">
            Log In
            </button>
        </div>      
      </nav>
    )
}

export default Navbar