# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model=pickle.load(open('D:/aditya python./Gold Price Prediction/trained model.sav','rb'))

print("Enter the values for the following features to predict the price of GLD:")
SPX = float(input())
USO = float(input())
SLV = float(input())
EURUSD = float(input())
input_data = np.array([[SPX, USO, SLV, EURUSD]])
predicted_value = loaded_model.predict(input_data)
print(f"\nThe predicted price of GLD based on the input values is: {predicted_value[0]}")