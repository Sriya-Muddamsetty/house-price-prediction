import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

model = pickle.load(open('LinearRegressionModel.pkl','rb'))
df = pd.read_csv('delhi_houses.csv')

st.title("House Price Prediction in Delhi")

rooms = st.number_input('Select number of rooms')
construction_status = st.selectbox('Choose construction status',['Under Construction','Ready to move'])
area = st.number_input('Select area in square ft')

status = 0
if construction_status == 'Under Construction':
    status = 1
else:
    status = 0


if st.button('Predict Price'):
    input = pd.DataFrame([[rooms, status, area]], columns=['Rooms', 'Status', 'Area'])
    st.success("The Predicted house price is ₹"+ str(int(model.predict(input)[0])))