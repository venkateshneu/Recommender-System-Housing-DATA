import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title="Viz Demo")

# Load the DataFrame
with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

# Load the prediction pipeline
with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs')

# Property type
property_type = st.selectbox('Property Type', ['flat', 'house'])

# Sector
sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

# Number of bedrooms
bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))

# Number of bathrooms
bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))

# Balconies
balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))

# Property age
property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

# Built-up area
built_up_area = float(st.number_input('Built Up Area'))

# Servant room
servant_room = float(st.selectbox('Servant Room', [0.0, 1.0]))

# Store room
store_room = float(st.selectbox('Store Room', [0.0, 1.0]))

# Furnishing type
furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

# Luxury score (updated)
luxury_score = st.selectbox('Luxury Score', sorted(df['luxury_score'].unique().tolist()))

# Floor category
floor_category = st.selectbox('Floor Category', sorted(df['floortype'].unique().tolist()))

if st.button('Predict'):
    # Form a DataFrame
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_score, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_score', 'floortype']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # Predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    # Display the prediction
    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low, 2), round(high, 2)))
