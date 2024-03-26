import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// NavBar import removed from here
import Footer from './components/Footer/footer';
import LandingPage from './pages/Landing'; // Assuming you combine Header, About, Testimonials into a single LandingPage component
import Login from './pages/Login';
import Signup from './pages/Signup';
import Signup2 from './pages/Signup2';
import Hub from './pages/Hub';
import Profile from './pages/Profile';
import Settings from './pages/Settings';
import Meals from './pages/Meals';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/signup2" element={<Signup2 />} />
          <Route path="/hub" element={<Hub />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/meals" element={<Meals />} />
          {/* Footer can still remain here if it's meant to be on every page */}
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
