import React from 'react';
import './navbar.css';
import logo from '../../../src/assets/iconWhite.png'
import { Link } from 'react-scroll'; //npmjs package

const Navbar = () => {
  return (
        <nav className="navbar">
            <img src={logo} alt="Logo" className='logo'/>
            <div className="desktopMenu">
              <Link to="intro" spy={true} smooth={true} offset={50} duration={500} className="desktopMenuListItem">Hub</Link>
              <Link to="/" spy={true} smooth={true} offset={50} duration={500} className="desktopMenuListItem">Products</Link>
              <Link to="skills" spy={true} smooth={true} offset={50} duration={500} className="desktopMenuListItem">About</Link>
            </div>
            <button className="desktopMenuBtn">
              Contact Me
            </button>
        </nav>
    )
}

export default Navbar