import './hubNav.css';
import React from 'react'

const hubnav = () => {
  return (
    <nav className='hubnav'>
        <div className='hubnavheader'>
          <a href="/hub" className="hubnavTab">Home</a>
          <a href="/meals" className="hubnavTab">Meals</a>
          <a href="/profile" className="hubnavTab">Profile</a>
          <a href="/settings" className="hubnavTab">Settings</a>       
        </div>
    </nav>
  )
}

export default hubnav