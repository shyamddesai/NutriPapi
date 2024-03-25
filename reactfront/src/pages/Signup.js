import React from 'react'
import Navbar from '../components/Login/NavBar/loginNavbar'
import SignUp from '../components/Signup/signup';

function Signup(){
    return(
        <div className="Signup">
            <Navbar/>
            <SignUp/>
        </div>
    );
}

export default Signup