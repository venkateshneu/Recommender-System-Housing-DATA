
# Real Estate Property Recommender System

## Project Overview

This project implements a real estate property recommendation engine designed to assist users in discovering the best-suited properties based on a variety of features. The system compares property details such as nearby locations, available facilities, and price ranges using advanced Natural Language Processing (NLP) and machine learning techniques. By utilizing **TF-IDF Vectorization** and **Cosine Similarity**, the system evaluates property similarity and ranks the recommendations accordingly. The application is deployed using **Streamlit** on **AWS EC2**, offering users real-time property suggestions.

## Key Features

- **NLP-Based Feature Comparison**: Leverages **TF-IDF Vectorization** to convert textual property data (e.g., facilities, nearby locations) into vectors for similarity calculations.
- **Cosine Similarity Calculation**: Provides personalized property recommendations by analyzing and ranking properties based on similarity scores.
- **Comprehensive Price Parsing**: Extracts and processes complex property pricing data for various configurations (e.g., 2 BHK, 3 BHK), ensuring accurate recommendations based on price.
- **Multi-Factor Recommendation**: Combines similarity across different features—facilities, locations, and price details—to deliver holistic property recommendations.
- **Real-Time Recommendation Engine**: Deployed via **Streamlit** on **AWS EC2**, the system is accessible in real-time, offering users instant property recommendations.

## Data Description

The dataset includes the following columns:

- **Property Name**: The official name of the property.
- **Nearby Locations**: A list of landmarks and important locations near the property, along with their respective distances.
- **Price Details**: Information about the price ranges for different property configurations, such as 2 BHK, 3 BHK, etc.
- **Top Facilities**: Details of the facilities offered by the property, including amenities like swimming pools, gyms, and security.

## How it Works

1. **Data Preprocessing**: The system cleans and processes property data by parsing text and transforming it into numerical vectors using **TF-IDF**. Facilities, location advantages, and price details are parsed and structured for analysis.
2. **Cosine Similarity**: The system calculates the similarity between different properties based on multiple factors, including features, location distances, and pricing.
3. **Property Recommendations**: The top five most similar properties are recommended based on their similarity scores, allowing users to easily discover properties that match their preferences.
4. **Real-Time Deployment**: The recommendation engine is deployed using **Streamlit** and hosted on **AWS EC2** to provide real-time, dynamic recommendations.

## Deployment

The system has been deployed via **Streamlit** on **AWS EC2**, allowing users to interact with the recommendation engine in real-time. By leveraging the cloud-based infrastructure of AWS, the system is capable of scaling efficiently and handling multiple user requests simultaneously.

## Conclusion

This project offers a powerful and efficient real estate property recommendation system that combines advanced NLP techniques with machine learning algorithms. The system delivers personalized property recommendations based on user preferences, all accessible in real-time through a simple and intuitive web interface.

