import './about.css'
import React from 'react'
import Logo from './../../../assets/iconS1080.png'

const about = () => {
  return (
    <div className='aboutBackground'>
        <section className='about'>
            <h1 className = 'aboutTitle'>About Us</h1>
            <div className='aboutBelowTitle'>
            <h4 className = 'aboutDesc'>Welcome to NutriPapi, where we revolutionize the way you approach health and fitness. Our platform offers a personalized recipe plan, tailored to your unique dietary needs and fitness goals. Simply input your current weight and desired outcomes, and we'll provide you with custom meal plans optimized for your target caloric intake. <br/><br/>
            At NutriPapi, we blend science with flavor, offering delicious, balanced meals designed by nutrition experts and culinary professionals. Whether your aim is to lose weight, gain muscle, or maintain a healthy lifestyle, our recipes are crafted to support your journey towards optimal health.<br/><br/>
            Embrace a lifestyle change with NutriPapi and take control of your health with nutrition that's customized just for you. Start your journey to a healthier, happier you today.
            </h4>
            <img src={Logo} alt="logo" className='aboutLogo'/>
            </div>

            
        </section>
    </div>
  )
}

export default about