import axios from 'axios';
import { useRouter } from 'next/router';
import React, { useState, ChangeEvent, FormEvent } from 'react';



const AuthPage = () => {
  const [isSignUp, setIsSignUp] = useState(true); // Toggle between sign up and sign in
  const [credentials, setCredentials] = useState({
    username: '',
    email: '',
    password: '',
  });
  const router = useRouter();

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setCredentials({ ...credentials, [name]: value });
  };


  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const url = isSignUp ? 'http://localhost:8000/api/signup/' : 'http://localhost:8000/api/signin/';
    
    try {
      const response = await axios.post(url, credentials);
      console.log(response.data);
      // Redirect to a new page upon success
      router.push('/dashboard'); // Modify as needed
    } catch (error: unknown) {
        if (error instanceof Error) {
          console.error('Error during authentication', error.message);
        } else {
          console.error('An unexpected error occurred', error);
        }
      }
}

  return (
    <div>
      <h1>{isSignUp ? 'Sign Up' : 'Sign In'}</h1>
      <form onSubmit={handleSubmit}>
        {isSignUp && (
          <input
            type="text"
            name="username"
            value={credentials.username}
            onChange={handleChange}
            placeholder="Username"
            required
          />
        )}
        <input
          type="email"
          name="email"
          value={credentials.email}
          onChange={handleChange}
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password"
          value={credentials.password}
          onChange={handleChange}
          placeholder="Password"
          required
        />
        <button type="submit">{isSignUp ? 'Sign Up' : 'Sign In'}</button>
      </form>
      <button onClick={() => setIsSignUp(!isSignUp)}>
        {isSignUp ? 'Already have an account? Sign In' : "Don't have an account? Sign Up"}
      </button>
    </div>
  );
};

export default AuthPage;
