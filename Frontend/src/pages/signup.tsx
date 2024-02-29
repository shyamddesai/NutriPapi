import axios from 'axios';
import { useRouter } from 'next/router';
import React, { useState, ChangeEvent, FormEvent } from 'react';
import styles from '/src/css/signup.module.css'


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
    const url = isSignUp ? 'http://localhost:8000/signup/' : 'http://localhost:8000/signin/';
    
    try {
        const response = await axios.post(url, credentials, { withCredentials: true });
        console.log(response.data);
        localStorage.setItem('userInfo', JSON.stringify(response.data));
        const redirectPage = isSignUp ? '/signup_follow' : '/dashboard';
        router.push(redirectPage);
    } catch (error: unknown) {
        if (error instanceof Error) {
          console.error('Error during authentication', error.message);
        } else {
          console.error('An unexpected error occurred', error);
        }
      }
}

    return (
        <div className={styles.container}>
            <div className={styles.formCard}>
                <h1 className={styles.formTitle}>{isSignUp ? 'Sign Up' : 'Sign In'}</h1>
                <form onSubmit={handleSubmit}>

                    {isSignUp && (
                        <div className={styles.inputField}>
                            <input
                                type="text"
                                name="username"
                                value={credentials.username}
                                onChange={handleChange}
                                placeholder="Username"
                                required
                            />
                        </div>
                    )}

                    <div className={styles.inputField}>
                        <input
                            type="email"
                            name="email"
                            value={credentials.email}
                            onChange={handleChange}
                            placeholder="Email"
                            required
                        />
                    </div>

                    <div className={styles.inputField}>
                        <input
                            type="password"
                            name="password"
                            value={credentials.password}
                            onChange={handleChange}
                            placeholder="Password"
                            required
                        />
                    </div>

                    <div className={styles.buttonContainer}>
                        <button type="submit" className={styles.submitButton}>
                            {isSignUp ? 'Sign Up' : 'Sign In'}
                        </button>
                    </div>

                </form>

                <div className={styles.buttonContainer}>
                    <button onClick={() => setIsSignUp(!isSignUp)} className={styles.submitButton}>
                        {isSignUp ? 'Already have an account? Sign In' : "Don't have an account? Sign Up"}
                    </button>
                </div>

            </div>
        </div>
    );
};

export default AuthPage;
