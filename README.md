# Women Football Result Prediction
Predicting the Score for Women's International Football Game


HDSC Summer ’23 Premier Project 
Team Matplotlib

The Women’s International Football Game is a captivating platform that highlights the remarkable skill, talent, and dedication of female athletes who compete at the highest level on the global stage. As the sport continues to grow and evolve, women's international football is a powerful catalyst for promoting gender equality and inspiring future generations of players. However, it is important to acknowledge that despite the sport's significance, women's international football has not received the same level of attention and analysis as its male counterpart. In an effort to shed light on this unexplored domain, our analysis of the provided dataset on women's international football results aims to bring forth valuable insights into the accomplishments and progress of female athletes in the sport. Through this exploration, we aim to elevate the recognition and appreciation of women's football on a broader scale.

About the Dataset

The dataset on women's international football has been obtained from Kaggle via the below link:
https://www.kaggle.com/datasets/martj42/womens-international-football-results

It consists of 4,884 recorded results of women's international football matches, including some international friendlies and tournaments. It includes the following columns:
date - date of the match
home_team - the name of the home team
away_team - the name of the away team
home_score - full-time home team score including extra time, not including penalty-shootouts
away_score - full-time away team score including extra time, not including penalty-shootouts
tournament - the name of the tournament
city - the name of the city/town/administrative unit where the match was played
country - the name of the country where the match was played
neutral - TRUE/FALSE column indicating whether the match was played at a neutral venue


Aim of this project

The primary objective of this project is to develop a robust regression model that utilizes the information contained in the seven other columns of the dataset to accurately predict the home and away scores of women's international football matches. By leveraging various regression techniques and utilizing the available features such as date, teams, tournament, city, country, and neutral venue, we aim to create a predictive model that can provide valuable insights into the expected outcomes of these matches.

Steps for the project

The project has been divided into the following steps:



Data Cleaning

In this step, we inspect for any missing or erroneous values. Fortunately, the dataset exhibits consistency as it lacks any null entries or duplicate records. However, a necessary adjustment involves transforming the date column from its previous object datatype to the appropriate datetime format, to ensure accurate analysis.

Exploratory Data Analysis

In the next step we gained valuable insights into the dataset through various visualizations and analyses and have listed down the key findings:

Home Score Distribution: Visualized the distribution of home scores using a histogram to understand the range and frequency of scores.
Statistical Analysis: Calculated the mean and median values of the 'home_score' column to assess the average and central tendency of home scores.
Tournament Participation: Explored the count of matches played in different tournaments, with a focus on the tournaments with the highest participation, such as UEFA Euro qualification and the Algarve Cup.

Team Performance Analysis: Identified the team with the most wins by comparing the 'home_score' and 'away_score' columns and counted the occurrences. Displayed the top five winning teams based on win counts.
Goal Difference Analysis: Examined the goal difference between winning and losing teams to understand the margin of victory. Found that the majority of matches had a goal difference of 1, indicating highly competitive matches.

High-Scoring Tournaments: Analyzed the goals per game (GPG) to assess the excitement and potential for witnessing more goals in different tournaments. Highlighted the OFC Nations Cup as having a significantly high average goals per game.
High-Scoring Teams: Identified the top 20 high-scoring countries based on goals per game in both home and away matches, considering teams with more than 30 matches for statistical validity.
Active Teams: Identified China as the most active home team, participating in over 175 matches, and Denmark as the most active away team, playing more than 140 matches.
Impact of the Pandemic: Examined the year 2020, which experienced a decline in the overall number of matches due to the global pandemic.
Popular Football Hosting Cities: Explored cities that are frequently used as venues for football matches, indicating a rich footballing culture and infrastructure.

Venue Types: Analyzed the proportion of matches played on neutral grounds versus non-neutral grounds, highlighting the importance of fairness and impartiality in international competitions. Approximately 44.2% of matches are played on neutral grounds, while 55.8% of matches take place on non-neutral grounds. This highlights the prevalence of international matches being played on neutral grounds compared to club matches.


These analyses and visualizations offer a comprehensive understanding of the dataset, shedding light on various aspects of women's international football and providing valuable insights for further exploration and interpretation.
 
Modelling and Evaluation

The third step  involves utilizing suitable regression models to train the dataset and make predictions for the home and away scores of the matches. To accomplish this, we exclude the home_score and away_score columns and focus on predicting these values based on the remaining seven columns. Considering that the month does not appear to hold significant relevance, we extract only the year information from the date column. Additionally, to harness the categorical values more effectively, we incorporate feature encoding techniques into our analysis. To explore various regression techniques, we train the data using multiple algorithms, including Linear Regression, Ridge Regression, Lasso Regression, ElasticNet, SGDRegressor, Decision Tree, and Random Forest. Performance assessment is conducted by comparing essential metrics such as mean squared error and R2 score. Among these algorithms, the Random Forest algorithm showcases the most promising performance. As a result, we select the Random Forest model as our final choice and employ GridSearchCV for hyperparameter tuning. By leveraging this process, we determine the optimal parameters for the model. This refined and fine-tuned Random Forest model is then used for the next step.

Deployment

In the deployment phase, we followed a systematic approach to deploy our model using Streamlit. First, we created a requirement file that included essential packages such as Streamlit, Pandas, Joblib, and Scikit-learn, ensuring that all dependencies are properly installed. Next, we developed the Streamlit file where the actual deployment of the model took place. This file was carefully designed to provide a user-friendly interface for interacting with the model and accessing its predictions. Then we proceeded to deploy it on the Streamlit Cloud platform, making it accessible to users over the internet. 

Conclusion

This project successfully developed a predictive model using a RandomForestRegressor to estimate the scores in football matches. The model achieved a satisfactory level of accuracy and demonstrated the importance of various features such as home team, away team, tournament, city, country, neutral ground, and year.
For future work, additional features could be explored, such as player statistics, team rankings, or weather conditions, to further enhance the model's predictive power. Additionally, incorporating advanced techniques like ensemble models or neural networks may be worth exploring for improved performance.
Looking back, a larger and more diverse dataset could have been beneficial for training the model, potentially capturing a wider range of scenarios and improving generalization. Moreover, a more extensive exploratory data analysis could have provided deeper insights and guided feature selection and engineering.
Overall, this project lays a solid foundation for predicting football match outcomes and opens avenues for further research and development in the field of sports analytics.


