import React from 'react'
import Nav from '../components/Login/NavBar/loginNavbar'
import HubNav from '../components/HubNav/hubNav'
import Profile from '../components/Profile/profile';

function profile() {
    return(
        <div className="profile">
            <Nav />
            <HubNav/>
            <Profile />
        </div>
    );
}

export default profile