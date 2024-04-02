import React from 'react'
import Nav from '../components/Login/NavBar/loginNavbar'
import HubNav from '../components/HubNav/hubNav'
import Recipes from '../components/Recipes/recipes';

function recipes() {
    return(
        <div className="recipes">
            <Nav />
            <HubNav/>
            <Recipes />
        </div>
    );
}

export default recipes