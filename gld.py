# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:19:11 2024

@author: Aditya
"""

import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('D:/aditya python/Gold Price Prediction/trained model.sav', 'rb'))

def gold_price_prediction(input_data):
    input_data = np.array(input_data)
    predicted_value = loaded_model.predict(input_data)
    return predicted_value[0]

def main():
    st.title("Gold Price Prediction Web Page")
    
    # Inputs for prediction
    SPX = st.text_input("SPX")
    USO = st.text_input("USO")
    SLV = st.text_input("SLV")
    EURUSD = st.text_input("EUR/USD")
    
    prediction = ''
    
    if st.button('Gold Price Prediction Result'):
        # Convert inputs to float and create input array
        try:
            input_data = [[float(SPX), float(USO), float(SLV), float(EURUSD)]]
            prediction = gold_price_prediction(input_data)
            st.success(f"The predicted price of GLD based on the input values is: {prediction}")
        except ValueError:
            st.error("Please enter valid numerical values for all fields.")
    
if __name__ == '__main__':
    main()
