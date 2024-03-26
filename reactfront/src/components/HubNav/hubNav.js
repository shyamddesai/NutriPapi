import './hubNav.css';
import React from 'react'

const hubnav = () => {
  return (
    <nav className='hubnav'>
        <div className='hubnavheader'>
          <a href="/hub" className="hubnavTab">Home</a>
          <a href="/hub/meals" className="hubnavTab">Meals</a>
          <a href="/hub/profile" className="hubnavTab">Profile</a>
          <a href="/hub/settings" className="hubnavTab">Settings</a>       
        </div>
    </nav>
  )
}

export default hubnav