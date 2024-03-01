import React from 'react'
import Navbar from '../components/Login/NavBar/loginNavbar'
import Footer from '../components/Footer/footer'
import SignUp from '../components/Signup/signup';

function Signup(){
    return(
        <div className="Signup">
            <Navbar/>
            <SignUp/>
            <Footer/>
        </div>
    );
}

export default Signup