import './hub.css'
import icon from './../../assets/userIcon.png'
import placeHolder from './../../assets/placeholderImage.png'
import React, { useState, useEffect } from 'react'
import axios from 'axios'

const Hub = () => {

    const [profilePhoto, setProfilePhoto] = useState(null);
    const [profilePhotoPreview, setProfilePhotoPreview] = useState(icon); // Use the icon as the default
    const [totalCalories, setTotalCalories] = useState(2700);
    const [currentWeight, setCurrentWeight] = useState(0);        
    const [targetWeight, setTargetWeight] = useState(0);
    const [weightLost, setWeightLost] = useState(0);
    const [weightToLose, setWeightToLose] = useState(0);
    const [dayStreak, setDayStreak] = useState(0);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
          setProfilePhoto(file);
          setProfilePhotoPreview(URL.createObjectURL(file));
        }
    };

    const uploadPhoto = async () => {
        if (!profilePhoto) return;
    
        const formData = new FormData();
        formData.append('profilePhoto', profilePhoto);
    
        try {
          // Adjust the URL to your API endpoint
          const response = await axios.post('/api/upload-photo', formData, {
            headers: {
              'Content-Type': 'multipart/form-data',
            },
          });
          // Handle the response, e.g., updating the profile photo URL state
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
    };

    useEffect(() => {
        const fetchCalories = async () => {
          try {
            const response = await axios.get('YOUR_ENDPOINT_URL');
            setTotalCalories(response.data.totalCalories); // Adjust according to your response structure
          } catch (error) {
            console.error("Failed to fetch calories", error);
          }
        };
      
        fetchCalories();
    }, []); // Empty dependency array means this runs once after initial render


    useEffect(() => {
        const fetchWeightData = async () => {
            try {
                const response = await axios.get('YOUR_WEIGHT_INFO_ENDPOINT');
                setCurrentWeight(response.data.currentWeight);
                setTargetWeight(response.data.targetWeight);
                setWeightLost(response.data.weightLost);
                setWeightToLose(response.data.targetWeight - response.data.currentWeight); // Assuming this calculation is correct for your case
            } catch (error) {
                console.error("Failed to fetch weight data", error);
            }
        };

        fetchWeightData();
    }, []); // Runs once after initial render

    useEffect(() => {
        const fetchStreakData = async () => {
            try {
                const response = await axios.get('YOUR_STREAK_INFO_ENDPOINT');
                setDayStreak(response.data.dayStreak);
            } catch (error) {
                console.error("Failed to fetch streak data", error);
            }
        };

        fetchStreakData();
    }, []);
    

      
    return (
        <div className='hubBackground'>
            <div className='hub'>
                <section className='hubSummary'>
                    
                    <header className='hubBodyHeader'>
                        Your Daily Summary
                    </header>
                    <body className='hubBody'>
                        <div className='hubSummaryPic'>
                            <img src={profilePhotoPreview} alt="Profile"></img>
                            <div>
                                {/* <input type="file" onChange={handleFileChange}></input> */}
                                {/* <button onClick={uploadPhoto}>Upload Photo</button> */}
                            </div>
                        </div>


                        <div className='hubSummaryCal'>
                            <div className='hubSummaryCalText'>
                                Total Calories for the Day:
                            </div>
                            <div className='hubSummaryCalCount'>
                                {totalCalories}
                            </div>
                        </div>


                        <div className='hubVerticalLine'></div>


                        <div className='hubSummaryWeight'>
                            <div className='hubSummaryWeights'>
                                Weight Lost So Far:
                                <div className='hubSummaryWeightNumber'>
                                    {weightLost} kgs
                                </div>
                            </div>
                            <div className='hubSummaryWeights'>
                                Weight To Lose:
                                <div className='hubSummaryWeightNumber'>
                                    {weightToLose} kgs
                                </div>
                            </div>
                            
                            
                            

                            
                            
                            <div className='hubSummaryStreakBox'>
                                <div className='hubSummaryStreakBoxText'>
                                    Day <br/> Streak:
                                </div>
                                <div className='hubSummaryStreakBoxDays'>
                                {dayStreak} days
                                </div>
                            </div>               

                        </div>

                    </body>
                </section>
                <section className='hubTodayMeal'>
                    <header className='hubBodyHeader'>
                        Today's Meal
                    </header>
                    <body className='hubBody'>

                    </body>
                </section>
                <section className='hubFridge'>
                    <header className='hubBodyHeader'>
                        My Fridge
                    </header>
                    <body className='hubBody'>
                        
                    </body>
                </section>    
            </div>
        </div>
    )
}

export default Hub