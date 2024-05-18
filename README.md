# HeartDiseasePrediction

A web application to predict heart disease using a Logistic Regression model. This application is built with Streamlit, providing an interactive interface for users to input their medical data and receive a prediction on whether they have heart disease.

## Features

- **Interactive Web App**: User-friendly interface to input medical data.
- **Machine Learning Model**: Logistic Regression model to predict heart disease.
- **Real-time Predictions**: Provides instant prediction results.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
   ```sh
   ggh repo clone jishnu2021/HeartDiseasePrediction
   cd HeartDiseasePrediction

2. **Install the required packages**:
   pip install -r requirements.txt

3. **Run the Streamlit app**:
   streamlit run app.py

## Usage
1. Open your web browser and go to http://localhost:8501.
2. Enter the required medical information into the input fields.
3. Click on the "Heart Disease Test Result" button to get the prediction.


## Files
1. web.py: The main application script for the Streamlit web app.
2. trainmodel.sav: The saved Logistic Regression model.
3. requirements.txt: A list of required packages for the application.

## Model Training

The Logistic Regression model is trained on a heart disease dataset. The training script is not included in this repository, but you can follow these general steps to train a similar model:

1. Load the dataset.
2. Preprocess the data (handle missing values, normalize features, etc.).
3. Split the data into training and testing sets.
4. Train a Logistic Regression model.
5. Save the trained model using pickle.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Streamlit

Scikit-learn
