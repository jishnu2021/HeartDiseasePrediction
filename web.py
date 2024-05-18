import numpy as np
import streamlit as st
import pickle

# Load the model
loaded_model = pickle.load(open('C:/Users/PC/Desktop/HeartDisease/trainmodel.sav','rb'))

def heartdiseaseprediction(input_data):
    input_npdata = np.asarray(input_data)
    inputdatareshape = input_npdata.reshape(1, -1)

    prediction = loaded_model.predict(inputdatareshape)

    if (prediction[0] == 0):
        return "The person does not have disease"
    else:
        return "The person has heart disease"

def main():
    st.title("Heart Disease Prediction Web App")
    
    # Collect user input
    age = st.text_input("Mention your Age")
    sex = st.text_input("Sex")
    cp = st.text_input("Cp")
    trestbps = st.text_input("Trestbps")
    chol = st.text_input("Cholesterol level")
    fbs = st.text_input("Fbs level")
    restecg = st.text_input("Restecg level")
    thalach = st.text_input("Thalach level")
    exang = st.text_input("Exang level")
    oldpeak = st.text_input("Oldpeak level")
    slope = st.text_input("Slope")
    ca = st.text_input("Ca level")
    thal = st.text_input("Thal level")
    
    disease = ''
    
    if st.button('Heart Disease Test Result'):
        try:
            # Convert inputs to float
            input_data = [
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]
            disease = heartdiseaseprediction(input_data)
        except ValueError:
            disease = "Please enter valid numeric values for all inputs."
        
    st.success(disease)

if __name__ == '__main__':
    main()
