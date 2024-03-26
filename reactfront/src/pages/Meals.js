import React from 'react'
import Nav from '../components/Login/NavBar/loginNavbar'
import HubNav from '../components/HubNav/hubNav'
import Meals from '../components/Meals/meals';

function meals() {
    return(
        <div className="settings">
            <Nav />
            <HubNav/>
            <Meals />
        </div>
    );
}

export default meals