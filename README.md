# Real Estate Property Recommendation and Price Prediction System
![GIF Preview](https://github.com/venkateshneu/Recommender-System-Housing-DATA/blob/main/Thursday_September19_2024at3_20_37PM_default_da42f633-ezgif.com-video-to-gif-converter.gif)

## Project Description
This project is a comprehensive solution for recommending real estate properties based on similarity metrics and predicting property prices. It leverages various techniques such as TF-IDF for textual analysis of top facilities, cosine similarity, and a combination of machine learning models for price prediction. The project uses AWS EC2 for deployment and Streamlit for real-time interaction.

### Features:
1. **Real-Time Property Recommendations**: Recommends similar properties based on property features and top facilities.
2. **Price Prediction**: Predicts property prices based on multiple features including area, location advantages, and amenities using multiple machine learning algorithms.
3. **Deployment**: Hosted on AWS EC2 with a real-time interface through Streamlit.

---

## Data Description
The dataset includes 246 rows and 7 columns with information on properties from Gurgaon. Key columns are:
- **PropertyName**: Name of the property.
- **TopFacilities**: List of the facilities provided in each property.
- **PriceDetails**: Price range and area information for different configurations (2 BHK, 3 BHK, etc.).
- **LocationAdvantages**: Key locations near the property along with distances.

---

## Preprocessing
1. **Data Cleaning**: Handled missing values and irrelevant columns. Columns such as `TopFacilities` were converted from list-like strings to proper lists for further analysis.
2. **Feature Engineering**: Extracted useful information such as building type, area, and price from the `PriceDetails` column and converted distances to meters in the `LocationAdvantages` column.
3. **One-Hot Encoding**: Applied One-Hot Encoding on categorical features such as property type and top facilities.
4. **Standardization**: Standardized all numerical features to ensure the data is on the same scale before training models.

---

## Modeling and Price Prediction

### 1. **TF-IDF Vectorization and Cosine Similarity for Recommendations**
- **TF-IDF Vectorizer**: Used to transform the `TopFacilities` column into a TF-IDF matrix.
- **Cosine Similarity**: Calculated similarity between different properties to recommend the top 5 most similar properties for any given property.

### 2. **Machine Learning Models for Price Prediction**
The following models were used for predicting property prices based on the engineered features:
- **Linear Regression**: Baseline model to predict prices using engineered features such as `area`, `building type`, and `location advantages`.
- **Ridge and Lasso Regression**: Regularized versions of linear regression to handle multicollinearity and improve prediction accuracy.
- **Random Forest and Gradient Boosting**: Used for capturing non-linear relationships in the data, improving predictive performance.
- **XGBoost**: Applied for further boosting accuracy, showing the best performance among ensemble methods.

The models were evaluated using R-squared (R²) and Mean Absolute Error (MAE) metrics.

### 3. **Dimensionality Reduction**
- **PCA (Principal Component Analysis)**: Applied to reduce dimensionality and improve model efficiency without losing significant information. 95% of the variance was retained.

### 4. **Cross-Validation**
- Performed 10-fold cross-validation for all machine learning models to ensure robustness of the predictions.

### Model Performance:
- **XGBoost**: Achieved the highest accuracy with R² = 0.89 and MAE = 0.57.
- **Random Forest**: Close second with R² = 0.88 and MAE = 0.58.

---

## Deployment
The project was deployed via **Streamlit** on an **AWS EC2** instance, providing real-time property recommendations and price predictions to the user through an interactive web interface.

---

## Installation Instructions
To run the project locally, follow these steps:
1. Clone the repository.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Streamlit app with `streamlit run app.py`.
4. Access the app at `http://localhost:8501` in your browser.

---

## Future Improvements
- Include a more comprehensive dataset covering a wider range of cities.
- Improve the recommendation system by integrating more advanced NLP techniques.
- Experiment with more advanced deep learning models for price prediction.
