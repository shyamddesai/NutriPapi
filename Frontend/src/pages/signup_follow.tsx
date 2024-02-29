import axios from 'axios';
import { useRouter } from 'next/router';
import React, { ChangeEvent, FormEvent, useState } from 'react';
import styles from '/src/css/signup_follow.module.css';


const SignupPage = () => {
    const [formData, setFormData] = useState({
        firstName: '',
        gender: '',
        goals: '',
        activityLevel: '',
        birthday: '1990-01-01',
        currentWeight: '',
        targetWeight: '',
        height: '',
        dietaryPreferences: ''
    });
    const router = useRouter();

    const handleChange = (e: ChangeEvent<HTMLInputElement> | ChangeEvent<HTMLSelectElement>) => {
        const { name, value } = e.target;
        setFormData(prevState => ({ ...prevState, [name]: value }));
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const url = 'http://localhost:8000/api/signup_follow/';

        try {
            const response = await axios.post(url, formData);
            console.log(formData);
            console.log(response.data);
            localStorage.setItem('userInfo', JSON.stringify(response.data));
            // router.push('fridge/add_ingredients/'); //  (TEMPORARY REDIRECT, CHANGE LATER) Redirect to the next page
        } catch (error) {
            console.error('Error during form submission:', error);
        }
    };

    return (
        <div className={styles.signupContainer}>
            <div className={styles.card}>
                <h1 className={styles.title}>Create an Account</h1>
                <form onSubmit={handleSubmit} className={styles.form}>
                    <input
                        type="text"
                        name="firstName"
                        placeholder="First Name"
                        value={formData.firstName}
                        onChange={handleChange}
                        required
                    />
                    <select
                        name="gender"
                        value={formData.gender}
                        onChange={handleChange}
                        required
                    >
                        <option value="">Select Gender</option>
                        <option value="male">Male</option>
                        <option value="female">Female</option>
                        <option value="other">Other</option>
                    </select>

                    <select
                        name="goals"
                        value={formData.goals}
                        onChange={handleChange}
                        required
                    >
                        <option value="health">Stay Healthy</option>
                        <option value="weight">Lose Weight</option>
                        <option value="muscle">Gain Muscle</option>
                        <option value="energy">Get Energized</option>
                    </select>

                    <select
                        name="activityLevel"
                        value={formData.activityLevel}
                        onChange={handleChange}
                        required
                    >
                        <option value="">Your Activity Level</option>
                        <option value="Temp">Temp</option>
                    </select>

                    <label htmlFor="birthday">Birthday:</label>
                    <input
                        type="date"
                        id="birthday"
                        name="birthday"
                        value={formData.birthday}
                        onChange={handleChange}
                        required
                    />

                    <input
                        type="number"
                        name="currentWeight"
                        value={formData.currentWeight}
                        onChange={handleChange}
                        step="1"
                        required
                    />

                    <input
                        type="number"
                        name="targetWeight"
                        value={formData.targetWeight}
                        onChange={handleChange}
                        step="1"
                        required
                    />

                    <input
                        type="number"
                        name="height"
                        value={formData.height}
                        onChange={handleChange}
                        step="1"
                        required
                    />

                    <select
                        name="dietaryPreferences"
                        value={formData.dietaryPreferences}
                        onChange={handleChange}
                        required
                    >
                        <option value="">Your Dietary Preference</option>
                        <option value="Temp">Temp</option>
                    </select>

                    <button type="submit" className={styles.button}>Continue</button>
                </form>
            </div>
        </div>
    );
};

export default SignupPage;