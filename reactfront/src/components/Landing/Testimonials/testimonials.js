import './testimonials.css'
import React from 'react'
import paddy from './../../../assets/paddy.png'
import masa from './../../../assets/masa.png'
import michelle from './../../../assets/michelle.png'


const testimonials = () => {
  return (
    <div className='testiBackground'>
      <section className='testi'>
        <h1 className='testiHeader'>
          Testimonials
        </h1>
        <div className='testiTexts'>
          <div className='testi1'>
            <div className='testiQuotes'>
              <h4 className='testiTopLeft'>"</h4>
              <h4>Nutri Papi has helped me balance my hectic life with my health goals. The recipes are quick, nutritious, and fit perfectly with my busy schedule. I feel healthier and more energized than ever before.</h4>
              <h4 className='testiBottomRight'>"</h4>
            </div>
            <div className='testiBody'>
            <img src={paddy} alt='paddy' className='ellipseLogo'/>
            <div className='testiBodyText'>
              <h2>Paddy Pimblett</h2>
              <h3>Fighter</h3>
            </div>
            </div>
          </div>

          <div className='testi2'>
            <div className='testiQuotes'>
              <h4 className='testiTopLeft'>"</h4>
              <h4>Nutri Papi has completely transformed my approach to nutrition and wellness. The personalized meal plans not only helped me reach my target weight but also introduced me to a whole new world of flavors. It's like having a dietitian and a chef right at your fingertips!</h4>
              <h4 className='testiBottomRight'>"</h4>
            </div>
            <div className='testiBody'>
            <img src={masa} alt='masa' className='ellipseLogo'/>
            <div className='testiBodyText'>
              <h2>Masa Kagami</h2>
              <h3>5x World Champion</h3>
            </div>
            </div>
          </div>

          <div className='testi3'>
            <div className='testiQuotes'>
              <h4 className='testiTopLeft'>"</h4>
              <h4>I was skeptical at first, but Nutri Papi proved me wrong. The ease of inputting my physical info and getting back a plan that actually fits my lifestyle and tastes is incredible. Plus, I've achieved my weight goals sooner than I expected. Highly recommend!</h4>
              <h4 className='testiBottomRight'>"</h4>
            </div>
            <div className='testiBody'>
            <img src={michelle} alt='michelle' className='ellipseLogo'/>
            <div className='testiBodyText'>
              <h2>Michelle Obama</h2>
              <h3>Lawyer</h3>
            </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}

export default testimonials