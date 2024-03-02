import React from 'react'
import Navbar from '../components/Login/NavBar/loginNavbar'
import Footer from '../components/Footer/footer'
import SignUp2 from '../components/Signup2/signup2';

function Signup2(){
    return(
        <div className="Signup2">
            <Navbar/>
            <SignUp2/>
            <Footer/>
        </div>
    );
}

export default Signup2