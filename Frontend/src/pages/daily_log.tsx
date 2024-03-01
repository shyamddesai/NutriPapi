import axios from 'axios';
import React, { useState, ChangeEvent, FormEvent } from 'react';
import styles from '/src/css/daily_log.module.css';

const LogPage = () => {
    const [mealLog, setMealLog] = useState({
        breakfast: '',
        lunch: '',
        dinner: '',
        exercise: '',
    });

    const [showSuccess, setShowSuccess] = useState(false);

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setMealLog({ ...mealLog, [name]: value });
    };

    const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const url = 'http://localhost:8000/log_meal';
        try {
            const response = await axios.post(url, mealLog, { withCredentials: true });
            console.log(response.data);
            setShowSuccess(true);
            setTimeout(() => setShowSuccess(false), 3000);
        } catch (error) {
            if (axios.isAxiosError(error) && error.response) {
                console.error('Error response', error.response.data);
            } else if (error instanceof Error) {
                console.error('Error message', error.message);
            } else {
                console.error('Unexpected error', error);
            }
        }
    };

    return (
        <div className={styles.logContainer}>
            <div className={styles.card}>
                <h1 className={styles.title}>Daily Log</h1>
                <form onSubmit={handleSubmit} className={styles.form}>
                    <div className={styles.inputGroup}>
                        <label htmlFor="breakfast" className={styles.label}>Breakfast</label>
                        <input
                            type="text"
                            id="breakfast"
                            name="breakfast"
                            value={mealLog.breakfast}
                            onChange={handleChange}
                            className={styles.inputField}
                            required
                        />
                    </div>

                    <div className={styles.inputGroup}>
                        <label htmlFor="lunch" className={styles.label}>Lunch</label>
                        <input
                            type="text"
                            id="lunch"
                            name="lunch"
                            value={mealLog.lunch}
                            onChange={handleChange}
                            className={styles.inputField}
                            required
                        />
                    </div>

                    <div className={styles.inputGroup}>
                        <label htmlFor="dinner" className={styles.label}>Dinner</label>
                        <input
                            type="text"
                            id="dinner"
                            name="dinner"
                            value={mealLog.dinner}
                            onChange={handleChange}
                            className={styles.inputField}
                            required
                        />
                    </div>

                    <div className={styles.inputGroup}>
                        <label htmlFor="exercise" className={styles.label}>Exercise</label>
                        <input
                            type="text"
                            id="exercise"
                            name="exercise"
                            value={mealLog.exercise}
                            onChange={handleChange}
                            className={styles.inputField}
                            required
                        />
                    </div>
                    <button type="submit" className={styles.submitButton}>Submit Log</button>
                </form>
            </div>

            {showSuccess && (
                <div className={styles.successNotification}>
                    Log submitted successfully!
                </div>
            )}
        </div>
    );
};

export default LogPage;