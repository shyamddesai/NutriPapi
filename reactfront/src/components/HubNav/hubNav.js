import './hubNav.css';
import React from 'react'

const hubnav = () => {
  return (
    <nav className='hubnav'>
        <div className='hubnavheader'>
          <div className='hubheaderHome'>
            Home
          </div>
          <div className='hubheaderMeals'>
            Meals
          </div>
          <div className='hubheaderProfile'>
            Profile
          </div>
          <div className='hubheaderSettings'>
            Settings
          </div>
          <div className='hubheader'>
            
          </div>
        </div>
    </nav>
  )
}

export default hubnav