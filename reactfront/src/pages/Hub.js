import React from 'react'
import NavBarHub from '../components/NavBarHub/navbarhub'
import HubNav from '../components/HubNav/hubNav'
import Hub from '../components/Hub/hub'

function hub(){
    return(
        <div className="hub">
            <NavBarHub />
            <HubNav/>
            <Hub/>
        </div>
    );
}

export default hub