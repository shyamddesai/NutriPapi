import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import NavBar from './components/NavBar/navbar'
import Footer from './components/Footer/footer'
import Header from './components/Landing/Header/header'
import About from './components/Landing/About/about'
import Testimonials from './components/Landing/Testimonials/testimonials'
import Login from './pages/Login'

function App() {
  return (
    <Router>
      <div className="App">
        <NavBar/>
        <Routes>
          <Route path="/" element={
            <>
              <Header/>
              <About/>
              <Testimonials/>
              <Footer/>
            </>
          } />
          <Route path="/login" element={<Login/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
