import React from 'react';
import './footer.css';

const Footer = () => {
  return (
    <div>
      <footer className='footerBackground'>
        <div className='footer'>
            <div className='slogan'>
              <div className='title'>
                NutriPapi
              </div>
              <div className='sloganText'>
                Find your healthy, and your happy.
              </div>
            </div>
            <div className='copyTextWrapper'>
              <div className='copyText'>
              Copyright &#169; 2024 NutriPapi. All right reserved.
              </div>
            </div>
            
        </div>
      </footer>
    </div>
  )
}

export default Footer