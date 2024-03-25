import Navbar from "../components/Login/NavBar/loginNavbar";
import LoginPage from "../components/Login/loginPage";

function Login(){
    return(
        <div className="Login">
            <Navbar/>
            <LoginPage/>
        </div>
    );
}

export default Login