import React from 'react';
import './footer.css';

const Footer = () => {
  return (
    <div>
      <footer className='footerBackground'>
        <div className='footer'>
            <div className='footerSlogan'>
              <div className='footerTitle'>
                NutriPapi
              </div>
              <div className='footerSloganText'>
                Find your healthy, and your happy.
              </div>
            </div>
            <div className='footerCopyTextWrapper'>
              <div className='footerCopyText'>
              Copyright &#169; 2024 NutriPapi. All right reserved.
              </div>
            </div>
            
        </div>
      </footer>
    </div>
  )
}

export default Footer