import pickle
import streamlit as st
import pandas as pd
import numpy as np
import sklearn as sk

clean_data=pd.read_csv('clean_data.csv')
pipe=pickle.load(open('pipe.pkl','rb'))

st.title('Bengalore House Price Predictor')
location=st.selectbox('Enter The Location Of The House',clean_data['location'].unique())
bhk=st.text_input('Enter The Bedroom/Hall/Kitchen Of The House')
sqft=st.text_input('Enter The Size(Sqft) Of The House')
bath=st.text_input('Enter The Bathroom Of The House')


if st.button('Predict'):
    predicted = pipe.predict(pd.DataFrame([[location, bhk, sqft, bath]], columns=['location', 'BHK', 'total_sqft', 'bath']))
    st.write('The Predicted Price is ',predicted[0],'Lakhs')