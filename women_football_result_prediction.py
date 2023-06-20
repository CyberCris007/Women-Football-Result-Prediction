import streamlit as st
import joblib
import category_encoders
import pandas as pd

# Load the trained models
home_model = joblib.load("home_score_model.pkl")
away_model = joblib.load("away_score_model.pkl")

# Create a function to encode features
def encode_features(features):
    features_df = pd.DataFrame([features], columns=["home_team", "away_team", "tournament", "city", "country", "neutral", "Year"])

    # Frequency Encoding
    features_df_copy = features_df.copy()
    columns_list = features_df.columns

    # Encode all columns
    for col in columns_list:
        # Encoder
        encoder = category_encoders.CountEncoder(cols=col, normalize=True)

        # Fit and transform
        features_df[col] = encoder.fit_transform(features_df[col])

    return features_df

# Streamlit app
def main():
    st.title("Women Football Match Predictor")
    st.write("Enter the following details:")

    # Input fields
    home_team = st.text_input("Home Team")
    away_team = st.text_input("Away Team")
    tournament = st.text_input("Tournament")
    city = st.text_input("City")
    country = st.text_input("Country")
    neutral = st.selectbox("Neutral", [True, False])
    year = st.number_input("Year", value=0, step=1)
    
    # Predict button
    if st.button("Predict"):
        features = [home_team, away_team, tournament, city, country, neutral, year]
        features_df = encode_features(features)

        # Predict home score
        home_score = home_model.predict(features_df)

        # Predict away score
        away_score = away_model.predict(features_df)

        # Determine the winner
        winner = home_team if home_score[0] > away_score[0] else away_team

        # Display predicted scores and likely winner
        st.write("Predicted Scores:")
        st.write(home_team, int(home_score[0]), ":", int(away_score[0]), away_team)
        st.write("Likely Winner:")
        st.write(winner, "is more likely to win the match!")

# Run the app
if __name__ == "__main__":
    main()
