import React from 'react'
// import Navbar from '../components/Login/NavBar/loginNavbar'
import NavBar from '../components/NavBar/navbar'
import Footer from '../components/Footer/footer'
import Hub from '../components/Hub/hub';

function hub(){
    return(
        <div className="hub">
            <NavBar/>
            <Hub/>
        </div>
    );
}

export default hub