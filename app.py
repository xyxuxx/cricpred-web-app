import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

#Streamlit page config
st.set_page_config(
    page_title='CricPred - Cricket Match Predictor',
    page_icon='./img/favicon.png',
    layout = 'centered',
    initial_sidebar_state = 'auto',
)


#nav
selected = option_menu(
    menu_title=None,
    options=['Home', 'Guide', 'T20', 'BPL', 'IPL', 'About'],
    icons=['bi bi-house', 'bi bi-file-earmark-fill', 'bi bi-cpu', 'bi bi-cpu', 'bi bi-cpu', 'bi bi-exclamation-square'],
    default_index=0,
    orientation='horizontal',
    )


# home
if selected == 'Home':
    st.html(
        "<h1 style='text-align: center;'><span style='color:#ff4b4b'>CricPred</span> - Cricket Match Predictor</h1>")
    st.html(
        "<p style='text-align: center;'>Step up to the crease and swing into the action! Get first-innings scores and match-winning probabilities faster than a T20 chase.</p>")

    st.html('''
            <h2>Welcome to your one-step cricket prediction platform!</h2>
    ''')
    st.html('''Welcome to CricPred, your ultimate destination for data-driven cricket predictions! Dive into the world of cricket like never before, 
    where each match comes alive with insights powered by historical data. From the strategic intensity of Test cricket to the fast-paced thrill of T20, 
    CricPred brings you predictions for every format, enhancing your game experience with analytical depth. <i style='color: #ff4b4b'>Let’s predict the game together!</i>''')

# guide
if selected == 'Guide':
    guide = st.selectbox('Select model for it\'s guide:',
                        ('T20 International Model', 'BPL Model',  'IPL Model'))

    if guide == 'T20 International Model':
        st.html('''
                        <h2>Guide for T20 International Match Prediction in CricPred</h2>
                        ''')
        st.markdown(
            '''
            1. **Choose Prediction Type:** Select either `1st innings Projected Score` or `Win probability based on 2nd innings`.
    
            2. Entering Match Details
            - Teams: Choose the batting and bowling teams from the dropdown lists.
            - Venue: Select the match venue from the provided options. 
            3. Input Match Stats: For both prediction types, enter the following match stats:
            - Overs completed: Number of overs completed.
            - Balls bowled: Total balls bowled so far.
            - Current runs: Runs scored by the batting team.
            - Wickets: Number of wickets lost by the batting team.
            - Last Five Overs Stats (`1st innings Projected Score`):
                - Runs scored in last five overs.
                - Wickets gone in last five overs.
            4. For the `Win probability based on 2nd innings` option, additional inputs include:
            - Target: The target score set by the first team.
            5. Generate Prediction
            - Click on `Predict`: After entering all inputs, click `Predict` to generate the prediction.
                - Projected Score (1st innings): Displays the estimated total score the batting team may achieve.
                - Win Probability (2nd innings): Shows the probability of either team winning based on the current match situation.
    
            `Note`: For predicting `1st innings Projected Score` of any match, you have the the match data till 5 overs at least.  
            '''
        )
    if guide == 'BPL Model':
        st.html('''
                            <h2>Guide for BPL Match Prediction in CricPred</h2>
                        ''')
        st.markdown(
            '''

            1. Entering Match Details
            - Teams: Choose the batting and bowling teams from the dropdown lists.
            - Venue: Select the match venue from the provided options. 
            2. Input Match Stats: 
            - Overs completed: Number of overs completed.
            - Balls bowled: Total balls bowled so far.
            - Current runs: Runs scored by the batting team.
            - Wickets: Number of wickets lost by the batting team.
            - Last Five Overs Stats:
                - Runs scored in last five overs.
                - Wickets gone in last five overs.
            3. Generate Prediction
            - Click on `Predict`: After entering all inputs, click `Predict` to generate the prediction.
                - Projected Score (1st innings): Displays the estimated total score the batting team may achieve.

            `Note`: For predicting `1st innings Projected Score` of any match, you have the the match data till 5 overs at least.  
            '''
        )
    if guide == 'IPL Model':
        st.html('''
                                <h2>Guide for IPL Match Prediction in CricPred</h2>
                                ''')
        st.markdown(
            '''
            1. **Choose Prediction Type:** Select either `1st innings Projected Score` or `Win probability based on 2nd innings`.

            2. Entering Match Details
            - Teams: Choose the batting and bowling teams from the dropdown lists.
            - Venue: Select the match venue from the provided options. 
            3. Input Match Stats: For both prediction types, enter the following match stats:
            - Overs completed: Number of overs completed.
            - Balls bowled: Total balls bowled so far.
            - Current runs: Runs scored by the batting team.
            - Wickets: Number of wickets lost by the batting team.
            - Last Five Overs Stats (`1st innings Projected Score`):
                - Runs scored in last five overs.
                - Wickets gone in last five overs.
            4. For the `Win probability based on 2nd innings` option, additional inputs include:
            - Target: The target score set by the first team.
            5. Generate Prediction
            - Click on `Predict`: After entering all inputs, click `Predict` to generate the prediction.
                - Projected Score (1st innings): Displays the estimated total score the batting team may achieve.
                - Win Probability (2nd innings): Shows the probability of either team winning based on the current match situation.

            `Note`: For predicting `1st innings Projected Score` of any match, you have the the match data till 5 overs at least.  
            '''
        )

# T20
if selected == 'T20':
    st.html('''
                <h2>T20 International Match Predictor</h2>
            ''')
    teams = ['Australia', 'Zimbabwe', 'India', 'Bangladesh', 'New Zealand',
             'South Africa', 'England', 'West Indies', 'Ireland', 'Afghanistan',
             'Pakistan', 'Sri Lanka', 'Netherlands']

    venue = ['AMI Stadium',
             'Adelaide Oval',
             'Al Amerat Cricket Ground Oman Cricket (Ministry Turf 1)',
             'Arnos Vale Ground, Kingstown, St Vincent',
             'Arun Jaitley Stadium, Delhi',
             'Barabati Stadium, Cuttack',
             'Barsapara Cricket Stadium, Guwahati',
             'Bay Oval, Mount Maunganui',
             'Beausejour Stadium, Gros Islet',
             'Bellerive Oval, Hobart',
             'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
             'Boland Park',
             'Brabourne Stadium',
             'Bready Cricket Club, Magheramason, Bready',
             'Brian Lara Stadium, Tarouba, Trinidad',
             'Brisbane Cricket Ground, Woolloongabba, Brisbane',
             'Buffalo Park',
             'Carrara Oval',
             'Castle Avenue, Dublin',
             'Central Broward Regional Park Stadium Turf Ground, Lauderhill',
             'Civil Service Cricket Club, Stormont, Belfast',
             'Coolidge Cricket Ground, Antigua',
             'County Ground, Bristol',
             'Daren Sammy National Cricket Stadium, Gros Islet, St Lucia',
             'De Beers Diamond Oval',
             'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
             'Dubai International Cricket Stadium',
             'Eden Gardens, Kolkata',
             'Eden Park, Auckland',
             'Edgbaston, Birmingham',
             'Feroz Shah Kotla',
             'GMHBA Stadium, South Geelong, Victoria',
             'Gaddafi Stadium, Lahore',
             'Grand Prairie Stadium, Dallas',
             'Grange Cricket Club Ground, Raeburn Place, Edinburgh',
             'Greater Noida Sports Complex Ground',
             'Green Park',
             'Greenfield International Stadium, Thiruvananthapuram',
             'Gymkhana Club Ground',
             'Hagley Oval, Christchurch',
             'Harare Sports Club',
             'Hazelaarweg',
             'Headingley, Leeds',
             'Himachal Pradesh Cricket Association Stadium, Dharamsala',
             'Holkar Cricket Stadium, Indore',
             'ICC Academy',
             'JSCA International Stadium Complex, Ranchi',
             'Jade Stadium',
             'John Davies Oval, Queenstown',
             'Kennington Oval, London',
             'Kensington Oval, Bridgetown, Barbados',
             'Kingsmead, Durban',
             "Lord's",
             'M Chinnaswamy Stadium, Bangalore',
             'MA Chidambaram Stadium, Chepauk',
             'Maharashtra Cricket Association Stadium, Pune',
             'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa',
             'Malahide, Dublin',
             'Mangaung Oval',
             'Manuka Oval, Canberra',
             'Maple Leaf North-West Ground',
             'McLean Park, Napier',
             'Melbourne Cricket Ground',
             'Moses Mabhida Stadium',
             'Narendra Modi Stadium, Ahmedabad',
             'Nassau County International Cricket Stadium, New York',
             "National Cricket Stadium, St George's, Grenada",
             'National Stadium, Karachi',
             'New Wanderers Stadium',
             'Newlands',
             'OUTsurance Oval',
             'Old Trafford, Manchester',
             'Pallekele International Cricket Stadium',
             'Perth Stadium',
             'Providence Stadium, Guyana',
             'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
             "Queen's Park Oval, Port of Spain",
             'Queens Sports Club, Bulawayo',
             'R.Premadasa Stadium, Khettarama',
             'Rajiv Gandhi International Cricket Stadium, Dehradun',
             'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
             'Rangiri Dambulla International Stadium',
             'Rawalpindi Cricket Stadium',
             'Riverside Ground, Chester-le-Street',
             'Sabina Park, Kingston, Jamaica',
             'Sardar Patel Stadium, Motera',
             'Saurashtra Cricket Association Stadium, Rajkot',
             'Sawai Mansingh Stadium, Jaipur',
             'Saxton Oval',
             'Seddon Park',
             'Seddon Park, Hamilton',
             'Senwes Park',
             'Shaheed Veer Narayan Singh International Stadium, Raipur',
             'Sharjah Cricket Stadium',
             'Sheikh Abu Naser Stadium',
             'Sheikh Zayed Stadium',
             'Shere Bangla National Stadium, Mirpur',
             'Simonds Stadium, South Geelong',
             'Sir Vivian Richards Stadium, North Sound, Antigua',
             'Sky Stadium, Wellington',
             'Sophia Gardens, Cardiff',
             'Sportpark Het Schootsveld',
             'Sportpark Westvliet, The Hague',
             "St George's Park, Gqeberha",
             'Stadium Australia',
             'Subrata Roy Sahara Stadium',
             'SuperSport Park, Centurion',
             'Sydney Cricket Ground',
             'Sylhet International Cricket Stadium',
             'The Rose Bowl, Southampton',
             'The Village, Malahide, Dublin',
             'The Wanderers Stadium, Johannesburg',
             'Trent Bridge, Nottingham',
             'University Oval, Dunedin',
             'VRA Ground',
             'Vidarbha Cricket Association Stadium, Jamtha, Nagpur',
             'Wankhede Stadium, Mumbai',
             'Warner Park, Basseterre, St Kitts',
             'Western Australia Cricket Association Ground',
             'Westpac Stadium',
             'Windsor Park, Roseau, Dominica',
             'Zahur Ahmed Chowdhury Stadium, Chattogram',
             'Zayed Cricket Stadium, Abu Dhabi',
             'Zhejiang University of Technology Cricket Field']


    proj_prob = st.selectbox('Select which type of prediction you want to see:',
                ('1st innings Projected Score', 'Win probability based on 2nd innings'))

    st.markdown(f'Fill the input values for: `{proj_prob}`')

    # 1st innings projected score
    if proj_prob == '1st innings Projected Score':
        col1, col2 = st.columns(2)
        with col1:
            batting_team = st.selectbox(
                'Batting Team',
                sorted(teams),
            )
        with col2:
            bowling_team = st.selectbox(
                'Bowling Team',
                sorted(teams),
            )


        venue = st.selectbox(
                'Venue',
                venue,
        )

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            over = st.number_input('Overs completed', format='%0.0f')
        with col2:
            ball = st.number_input('Balls bowled', format='%0.0f')
        with col3:
            wickets = st.number_input('Wickets', format='%0.0f')
        with col4:
            current_runs = st.number_input('Current runs', format='%0.0f')

        col1, col2 = st.columns(2)
        with col1:
            last_five_runs = st.number_input('Runs scored in last five overs', format='%0.0f')
        with col2:
            last_five_wicket = st.number_input('Wickets gone in last five overs', format='%0.0f')

        if st.button('Predict', type='primary'):
            if batting_team != bowling_team:
                balls_left = 120 - ((over * 6) + ball)
                wickets_left = 10 - wickets
                crr = (current_runs * 6) / ((over * 6) + ball)

                df = pd.DataFrame({'batting_team':[batting_team],
                                   'bowling_team':[bowling_team],
                                   'venue':[venue],
                                   'balls_left':[balls_left],
                                   'wickets_left':[wickets_left],
                                   'current_runs':[current_runs],
                                   'current_run_rate':[crr],
                                   'last_five_runs':[last_five_runs],
                                   'last_five_wickets':[last_five_wicket]})

                model = pickle.load(open('models/t20_proj_model.pkl', 'rb'))
                pred_score = model.predict(df)

                st.subheader(f'Projected Score: {round(pred_score[0])}', anchor=False)

    # win probability based on 2nd innings
    if proj_prob == 'Win probability based on 2nd innings':
        col1, col2 = st.columns(2)
        with col1:
            batting_team = st.selectbox(
                'Batting Team',
                sorted(teams),
            )
        with col2:
            bowling_team = st.selectbox(
                'Bowling Team',
                sorted(teams),
            )


        venue = st.selectbox(
                'Venue',
                (venue),
        )


        col1, col2 = st.columns(2)
        with col1:
            target = st.number_input('Target', format='%0.0f')
        with col2:
            current_runs = st.number_input('Current runs', format='%0.0f')

        col1, col2, col3 = st.columns(3)
        with col1:
            over = st.number_input('Overs completed', format='%0.0f')
        with col2:
            ball = st.number_input('Balls bowled', format='%0.0f')
        with col3:
            wickets = st.number_input('Wickets', format='%0.0f')


        if st.button('Predict', type='primary'):
            if batting_team != bowling_team:
                balls_left = 120 - ((over * 6) + ball)
                wickets_left = 10 - wickets
                crr = (current_runs * 6) / ((over * 6) + ball)
                rrr = ((target - current_runs) * 6) / balls_left


                df = pd.DataFrame({'batting_team':[batting_team],
                                   'bowling_team':[bowling_team],
                                   'venue':[venue],
                                   'target':[target],
                                   'balls_left':[balls_left],
                                   'wickets_left':[wickets_left],
                                   'current_runs':[current_runs],
                                   'current_run_rate':[crr],
                                   'required_run_rate':[rrr]})

                model = pickle.load(open('models/t20_win_prob_model.pkl', 'rb'))

                t20_win_prob = model.predict_proba(df)
                win = t20_win_prob[0][1] * 100
                loss = t20_win_prob[0][0] * 100

                st.subheader(f'{batting_team} : {round(win)}%', anchor=False)
                st.subheader(f'{bowling_team} : {round(loss)}%', anchor=False)

# BPL
if selected == 'BPL':
    st.html('''
                <h2>Bangladesh Premier League (BPL) Match Predictor</h2>
            ''')
    teams = ['Rangpur Riders',
             'Fortune Barishal',
             'Dhaka Capitals',
             'Durbar Rajshahi',
             'Chittagong Kings',
             'Khulna Tigers',
             'Sylhet Strikers']

    venue = ['MA Aziz Stadium, Chittagong',
             'Sheikh Abu Naser Stadium, Khulna',
             'Shere Bangla National Stadium, Mirpur',
             'Sylhet International Cricket Stadium',
             'Zahur Ahmed Chowdhury Stadium, Chittagong']




    st.markdown(f'Fill the input values for: `1st innings Projected Score`')

    # 1st innings projected score
    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox(
                    'Batting Team',
                    sorted(teams),
                )
    with col2:
        bowling_team = st.selectbox(
                    'Bowling Team',
                    sorted(teams),
                )


    venue = st.selectbox(
                    'Venue',
                    venue,
            )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        over = st.number_input('Overs completed', format='%0.0f')
    with col2:
        ball = st.number_input('Balls bowled', format='%0.0f')
    with col3:
        wickets = st.number_input('Wickets', format='%0.0f')
    with col4:
        current_runs = st.number_input('Current runs', format='%0.0f')

    col1, col2 = st.columns(2)
    with col1:
        last_five_runs = st.number_input('Runs scored in last five overs', format='%0.0f')
    with col2:
        last_five_wicket = st.number_input('Wickets gone in last five overs', format='%0.0f')

    if st.button('Predict', type='primary'):
        if batting_team != bowling_team:
            balls_left = 120 - ((over * 6) + ball)
            wickets_left = 10 - wickets
            crr = (current_runs * 6) / ((over * 6) + ball)

            df = pd.DataFrame({'batting_team':[batting_team],
                                'bowling_team':[bowling_team],
                                'venue':[venue],
                                'balls_left':[balls_left],
                                'wickets_left':[wickets_left],
                                'current_runs':[current_runs],
                                'current_run_rate':[crr],
                                'last_five_runs':[last_five_runs],
                                'last_five_wickets':[last_five_wicket]})

            model = pickle.load(open('models/bpl_proj_model.pkl', 'rb'))
            pred_score = model.predict(df)

            st.subheader(f'Projected Score: {round(pred_score[0])}', anchor=False)

# IPL
if selected == 'IPL':
    st.html('''
                <h2>Indian Premier League(IPL) Match Predictor</h2>
            ''')
    teams = ['Royal Challengers Bengaluru', 'Kolkata Knight Riders',
             'Delhi Capitals', 'Sunrisers Hyderabad', 'Mumbai Indians',
             'Punjab Kings', 'Gujarat Titans', 'Chennai Super Kings',
             'Rajasthan Royals', 'Lucknow Super Giants']

    venue = ['Arun Jaitley Stadium, Delhi',
             'Barabati Stadium',
             'Barsapara Cricket Stadium, Guwahati',
             'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow',
             'Brabourne Stadium, Mumbai',
             'De Beers Diamond Oval',
             'Dr DY Patil Sports Academy, Mumbai',
             'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
             'Eden Gardens, Kolkata',
             'Feroz Shah Kotla',
             'Himachal Pradesh Cricket Association Stadium, Dharamsala',
             'Holkar Cricket Stadium',
             'JSCA International Stadium Complex',
             'M Chinnaswamy Stadium, Bengaluru',
             'MA Chidambaram Stadium, Chepauk, Chennai',
             'Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur',
             'Maharashtra Cricket Association Stadium, Pune',
             'Narendra Modi Stadium, Ahmedabad',
             'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
             'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
             'Sardar Patel Stadium, Motera',
             'Saurashtra Cricket Association Stadium',
             'Sawai Mansingh Stadium, Jaipur',
             'Shaheed Veer Narayan Singh International Stadium',
             'Subrata Roy Sahara Stadium',
             'Vidarbha Cricket Association Stadium, Jamtha',
             'Wankhede Stadium, Mumbai']


    proj_prob = st.selectbox('Select which type of prediction you want to see:',
                ('1st innings Projected Score', 'Win probability based on 2nd innings'))

    st.markdown(f'Fill the input values for: `{proj_prob}`')

    # 1st innings projected score
    if proj_prob == '1st innings Projected Score':
        col1, col2 = st.columns(2)
        with col1:
            batting_team = st.selectbox(
                'Batting Team',
                sorted(teams),
            )
        with col2:
            bowling_team = st.selectbox(
                'Bowling Team',
                sorted(teams),
            )


        venue = st.selectbox(
                'Venue',
                venue,
        )

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            over = st.number_input('Overs completed', format='%0.0f')
        with col2:
            ball = st.number_input('Balls bowled', format='%0.0f')
        with col3:
            wickets = st.number_input('Wickets', format='%0.0f')
        with col4:
            current_runs = st.number_input('Current runs', format='%0.0f')

        col1, col2 = st.columns(2)
        with col1:
            last_five_runs = st.number_input('Runs scored in last five overs', format='%0.0f')
        with col2:
            last_five_wicket = st.number_input('Wickets gone in last five overs', format='%0.0f')

        if st.button('Predict', type='primary'):
            if batting_team != bowling_team:
                balls_left = 120 - ((over * 6) + ball)
                wickets_left = 10 - wickets
                crr = (current_runs * 6) / ((over * 6) + ball)

                df = pd.DataFrame({'batting_team':[batting_team],
                                   'bowling_team':[bowling_team],
                                   'venue':[venue],
                                   'balls_left':[balls_left],
                                   'wickets_left':[wickets_left],
                                   'current_runs':[current_runs],
                                   'current_run_rate':[crr],
                                   'last_five_runs':[last_five_runs],
                                   'last_five_wickets':[last_five_wicket]})

                model = pickle.load(open('models/ipl_proj_model.pkl', 'rb'))
                pred_score = model.predict(df)

                st.subheader(f'Projected Score: {round(pred_score[0])}', anchor=False)

    # win probability based on 2nd innings
    if proj_prob == 'Win probability based on 2nd innings':
        col1, col2 = st.columns(2)
        with col1:
            batting_team = st.selectbox(
                'Batting Team',
                sorted(teams),
            )
        with col2:
            bowling_team = st.selectbox(
                'Bowling Team',
                sorted(teams),
            )


        venue = st.selectbox(
                'Venue',
                (venue),
        )


        col1, col2 = st.columns(2)
        with col1:
            target = st.number_input('Target', format='%0.0f')
        with col2:
            current_runs = st.number_input('Current runs', format='%0.0f')

        col1, col2, col3 = st.columns(3)
        with col1:
            over = st.number_input('Overs completed', format='%0.0f')
        with col2:
            ball = st.number_input('Balls bowled', format='%0.0f')
        with col3:
            wickets = st.number_input('Wickets', format='%0.0f')


        if st.button('Predict', type='primary'):
            if batting_team != bowling_team:
                balls_left = 120 - ((over * 6) + ball)
                wickets_left = 10 - wickets
                crr = (current_runs * 6) / ((over * 6) + ball)
                rrr = ((target - current_runs) * 6) / balls_left


                df = pd.DataFrame({'batting_team':[batting_team],
                                   'bowling_team':[bowling_team],
                                   'venue':[venue],
                                   'target':[target],
                                   'balls_left':[balls_left],
                                   'wickets_left':[wickets_left],
                                   'current_runs':[current_runs],
                                   'current_run_rate':[crr],
                                   'required_run_rate':[rrr]})

                model = pickle.load(open('models/ipl_prob_model.pkl', 'rb'))

                t20_win_prob = model.predict_proba(df)
                win = t20_win_prob[0][1] * 100
                loss = t20_win_prob[0][0] * 100

                st.subheader(f'{batting_team} : {round(win)}%', anchor=False)
                st.subheader(f'{bowling_team} : {round(loss)}%', anchor=False)


# About
if selected == "About":

    st.markdown('''This app aims to predict `men's` cricket match outcomes across international and 
                club-level matches. Leveraging extensive historical data, this app provides fans and analysts with insights into game results, 
                factoring in team performance, and match conditions. From Tests to T20s, this predictive tool brings data-driven excitement to every 
                cricket match.''', unsafe_allow_html=True)
    st.html('''
                <h2>About The Models</h2>
            ''')
    model_info = st.selectbox('Select Model: ',
                              ('T20 International Model', 'BPL Model', 'IPL Model'))
    if model_info == 'T20 International Model':
        st.markdown(
            '''
            `**` T20 Model: `1st Innings Projected Score`
                
            After performing 10 cross-validations on the model, the following metrics have been achieved:
                
            - Mean Absolute Error (MAE): 1.88 – This metric indicates that, `on average`, the model's predictions deviate from the actual values by about 1.88 units.
            
            - Root Mean Squared Error (RMSE): 3.77 – This metric demonstrates that `on average`, model's predicted values differ from the actual values by 3.77 units.
            
            - R² Score: 98.75% – This metric score signifies that `on average`, our model explains 98.75% of the variance in the data, reflecting strong predictive power and high model reliability.
                    
            T20 Model: `Win Probability based on 2nd Innings`
                    
            After performing 10 cross-validations on the model, the following metrics have been achieved:
            
            - Accuracy Score: 84% – This metric indicates that, on average, the model correctly predicts the outcome in approximately 84 out of every 100 cases during the training phase.
            '''
        )
    if model_info == 'BPL Model':
        st.markdown(
            '''
            `**` BPL Model: `1st Innings Projected Score`
            
            After performing 10 cross-validations on the model, the following metrics have been achieved:
            
            - Mean Absolute Error (MAE): 2.90 – This metric indicates that, `on average`, the model's predictions deviate from the actual values by about 2.90 units.
            
            - Root Mean Squared Error (RMSE): 5.66 – This metric demonstrates that `on average`, model's predicted values differ from the actual values by 5.66 units.
            
            - R² Score: 96.5% – This metric score signifies that `on average`, our model explains 96.5% of the variance in the data, reflecting strong predictive power and high model reliability.
            '''
        )
    if model_info == 'IPL Model':
        st.markdown(
            '''
            `**` IPL Model: `1st Innings Projected Score`

            After performing 10 cross-validations on the model, the following metrics have been achieved:

            - Mean Absolute Error (MAE): 2.70 – This metric indicates that, `on average`, the model's predictions deviate from the actual values by about 2.70 units.

            - Root Mean Squared Error (RMSE): 5.42 – This metric demonstrates that `on average`, model's predicted values differ from the actual values by 5.66 units.

            - R² Score: 97% – This metric score signifies that `on average`, our model explains 97% of the variance in the data, reflecting strong predictive power and high model reliability.
            
            IPL Model: `Win Probability based on 2nd Innings`
                    
            After performing 10 cross-validations on the model, the following metrics have been achieved:
            
            - Accuracy Score: 82% – This metric indicates that, on average, the model correctly predicts the outcome in approximately 82 out of every 100 cases during the training phase.
            '''

        )

# Footer
footer = """
<style>
footer {
    visibility: hidden;
}
.stylish-footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    height: 40px;
    background-color: #1E1E1E;
    color: #FFFFFF;
    text-align: center;
    font-size: 12px;
    padding: 5px; 
}

</style>

<div class="stylish-footer">
    <p> Thank you for visiting | © 2024 | Ideas from CampusX | <a href="https://github.com/xyxuxx" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-github" viewBox="0 0 16 16">
  <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8"/>
</svg></a> | <a href="mailto:syfullah.shifat@gmail.com"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
  <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1zm13 2.383-4.708 2.825L15 11.105zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741M1 11.105l4.708-2.897L1 5.383z"/>
</svg></a></p>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
