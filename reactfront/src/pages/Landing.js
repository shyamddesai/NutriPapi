import React from 'react'
import NavBar from '../components/NavBar/navbar'
import About from '../components/Landing/About/about'
import Header from '../components/Landing/Header/header'
import Testmonials from '../components/Landing/Testimonials/testimonials'

function landing(){
    return(
        <div className="hub">
            <NavBar/>
            <Header/>
            <About/>
            <Testmonials/>
        </div>
    );
}

export default landing