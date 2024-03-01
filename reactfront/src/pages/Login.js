import Navbar from "../components/Login/NavBar/loginNavbar";
import Footer from "../components/Login/Footer/loginfooter";
import LoginPage from "../components/Login/loginPage";

function Login(){
    return(
        <div className="Login">
            <Navbar/>
            <LoginPage/>
            <Footer/>
        </div>
    );
}

export default Login