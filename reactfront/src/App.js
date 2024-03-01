import NavBar from './components/NavBar/navbar'
import Footer from './components/Footer/footer'
import Header from './components/Landing/Header/header'
import About from './components/Landing/About/about'
import Testimonials from './components/Landing/Testimonials/testimonials'

function App() {
  return (
    <div className="App">
      <NavBar/>
      <Header/>
      <About/>
      <Testimonials/>
      <Footer/>
    </div>
  );
}

export default App;
