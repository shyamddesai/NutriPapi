import React from 'react'
import Nav from '../components/Login/NavBar/loginNavbar'
import HubNav from '../components/HubNav/hubNav'
import Log from '../components/Log/log';

function log() {
    return(
        <div className="log">
            <Nav />
            <HubNav/>
            <Log />
        </div>
    );
}

export default log