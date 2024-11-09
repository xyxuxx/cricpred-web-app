# CricPred - Cricket Match Predictor

A comprehensive, Streamlit-based web application for predicting cricket match outcomes across various leagues and formats, including T20 Internationals, Bangladesh Premier League (BPL), and Indian Premier League (IPL). 

## Overview
CricPred provides accurate predictions for both first-innings projected scores and win probabilities during the second innings, based on real-time data inputs. Utilizing different machine learning models tailored to each league and match type, CricPred delivers insights for fans and analysts, enhancing the cricket experience with data-driven predictions.

## Dataset 
This project was made possible with the detailed and well-organized cricket dataset provided by [Cricsheet](https://cricsheet.org/). Cricsheet’s commitment to offering ball-by-ball data for a wide range of international and club matches has been essential in developing the prediction model and enhancing the accuracy of the app.


## Features
- **Internationals and Leagues Supported**:
  - **T20 Internationals**
  - **Bangladesh Premier League (BPL)**
  - **Indian Premier League (IPL)**

- **Prediction Options**:
  - **For T20 Internationals and IPL:**
    - **1st Innings Projected Score**: Predicts the score at the end of the first innings based on current match situation.
    - **Win Probability (2nd Innings)**: Provides winning probabilities based on the target and current match situation.
  - **For BPL:**
    - **1st Innings Projected Score**: Predicts the likely score at the end of the first innings based on current match situation.
    

- **Guided Input**: Step-by-step guidance for entering match details, including team selection, venue, overs, balls bowled, current runs, and wickets.
- **Model Performance**: Provided all models performance based on multiple cross validations.
  

## Evaluation Metrics:
- **T20 Model**:
    - 1st Innings Projected Score: 
        - R² Score: 98.75%, 
        - MAE: 1.88, 
        - RMSE: 3.77
    - Win Probability (2nd Innings): 
        - Accuracy: 84%
- **BPL Model**:
    - 1st Innings Projected Score: 
        - R² Score: 96.5%, 
        - MAE: 2.90, 
        - RMSE: 5.66
- **IPL Model**:
    - 1st Innings Projected Score: 
        - R² Score: 97%, 
        - MAE: 2.70, 
        - RMSE: 5.42
    - Win Probability (2nd Innings): 
        - Accuracy: 82%

## License
(MIT License)[LICENSE]