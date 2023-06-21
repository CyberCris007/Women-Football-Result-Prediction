import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained models
home_model = joblib.load("/home/boniface/Desktop/Projects/Women-Football-Result-Prediction/home_model.pkl")
away_model = joblib.load("/home/boniface/Desktop/Projects/Women-Football-Result-Prediction/away_model.pkl")

# Load the features
features = pd.read_csv('/home/boniface/Desktop/Projects/Women-Football-Result-Prediction/features.csv')

# Create dictionaries for storing the mappings
mappings = {}

# Encode all columns
for col in features.columns:
    # Create a label encoder
    encoder = LabelEncoder()
    
    # Fit and transform the column
    features[col] = encoder.fit_transform(features[col])     
    
    # Create a dictionary mapping the categories to their encoded values
    mapping = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))
    
    # Store the mapping dictionary
    mappings[col] = mapping

# Create a function to encode features
def encode_features(features, mappings):
    columns_list = features.columns
    encoded_input = []

    # Iterate over each item in the input array
    for i, item in enumerate(features.values[0]):
        # Check if the item's column exists in the mappings dictionary
        if columns_list[i] in mappings:
            # Get the encoded value for the category using the mappings dictionary
            encoded_value = mappings[columns_list[i]].get(item, -1)  # Use -1 as a default value if the category is not found in mappings
            encoded_input.append(encoded_value)
        else:
            encoded_input.append(item)  # If the column is not categorical, keep the original value

    input_row = pd.DataFrame([encoded_input], columns=['home_team', 'away_team', 'tournament', 'city', 'country','neutral','Year'])
    return input_row

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
        input_features = [home_team, away_team, tournament, city, country, neutral, year]
        encoded_input = encode_features(pd.DataFrame([input_features], columns=['home_team', 'away_team', 'tournament', 'city', 'country','neutral','Year']), mappings)

        # Predict home score
        home_score = home_model.predict(encoded_input)

        # Predict away score
        away_score = away_model.predict(encoded_input)

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
