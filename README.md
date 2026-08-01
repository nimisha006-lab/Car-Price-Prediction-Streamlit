# Car Price Prediction Web App

**Name:** *Nimisha Roy*
**MUID:** *nimisharoy@mulearn*

## PROJECT OVERVIEW

This project predicts the selling price of used cars using Machine Learning. The Cardekho dataset was cleaned and preprocessed before training multiple regression models. Three machine learning algorithms—Linear Regression, Decision Tree Regressor, and Random Forest Regressor—were evaluated. Based on performance metrics, the Random Forest model was selected as the final model because it achieved the highest prediction accuracy. The trained model was then deployed as an interactive web application using Streamlit.

## DEPLOYMENT APPROACH

The trained Random Forest model was saved using Joblib (`model.pkl`), and the label encoders used during preprocessing were saved as `encoders.pkl`. A Streamlit web application (`app.py`) was developed to provide a simple user interface where users can enter car details and receive an estimated selling price instantly.

## TECHNOLOGIES USED

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Joblib

## KEY OBSERVATIONS

* Random Forest achieved the best performance among all the models.
* Proper data preprocessing improved the model's prediction accuracy.
* Encoding categorical variables was essential for successful model training.
* Saving both the trained model and encoders ensured consistent predictions during deployment.
* The Streamlit application allows users to make predictions through an interactive interface.

## CHALLENGES FACED

* Cleaning and preprocessing the dataset.
* Encoding categorical features correctly.
* Managing encoders during deployment.
* Fixing Streamlit layout and widget-related issues.
* Ensuring the input features matched the model's training data.
* Debugging prediction and deployment errors.

## FUTURE IMPROVEMENTS

* Replace Label Encoding with One-Hot Encoding or a preprocessing pipeline.
* Improve the Streamlit interface with additional styling and visualizations.
* Add feature importance charts to explain model predictions.
* Include input validation for better user experience.
* Deploy future versions with additional features and improved scalability.

## PROJECT STRUCTURE

README.md

Car-Price-Prediction-App/
│
├── app.py
├── model.pkl
├── encoders.pkl
├── requirements.txt
├── training.ipynb
└── cardekho_dataset.csv
