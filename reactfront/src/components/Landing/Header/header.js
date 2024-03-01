import './header.css';
import React from 'react'
import Fruits from './../../../assets/fruit.png'

export const header = () => {
  return (
    <header className='headerBackground'>
        <div className='header'>
            <div className='text'>
                <div className='subTitle'>
                    EAT SMARTER. GET FITTER.
                </div>
                <div className='title'>
                    Tailored Nutrition, <br/>
                    for Your Unique <br/>
                    LifeStyle
                </div>
                <div className="desc">
                    Input your goals, and let's tailor your path to a healthier you with custom recipe plans.
                </div>
                <button className='btn'>
                    Try For Free
                </button>
            </div>
            <div className='image'>
                <img src={Fruits} alt="fruits" className='Fruits'/>
            </div>
        </div>
    </header>

  )
}

export default header;
