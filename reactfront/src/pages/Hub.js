import React from 'react'
import Hub from '../components/Hub/hub'
import HubNav from '../components/HubNav/hubNav'
import Nav from '../components/Login/NavBar/loginNavbar'
// import Nav from '../components/NavBar/navbar'

function hub(){
    return(
        <div className="hub">
            <Nav />
            <HubNav/>
            <Hub/>
        </div>
    );
}

export default hub