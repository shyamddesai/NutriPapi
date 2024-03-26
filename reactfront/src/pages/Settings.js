import React from 'react'
import NavBarHub from '../components/NavBarHub/navbarhub'
import HubNav from '../components/HubNav/hubNav'
import Settings from '../components/Settings/settings';

function settings() {
    return(
        <div className="settings">
            <NavBarHub />
            <HubNav/>
            <Settings />
        </div>
    );
}

export default settings