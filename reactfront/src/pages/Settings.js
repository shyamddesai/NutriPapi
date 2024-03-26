import React from 'react'
import Nav from '../components/Login/NavBar/loginNavbar'
import HubNav from '../components/HubNav/hubNav'
import Settings from '../components/Settings/settings';

function settings() {
    return(
        <div className="settings">
            <Nav />
            <HubNav/>
            <Settings />
        </div>
    );
}

export default settings