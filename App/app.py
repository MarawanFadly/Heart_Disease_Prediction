import os
import numpy as np
import pandas as pd
import streamlit as st      # streamlit run app/app.py
import joblib 
import pickle

model= joblib.load("../Artifacts/parkinson_model.pkl")

st.set_page_config( 'Exam Score Prediction', ':book:', 'wide' )

#### Setting a background color to a streamlit page

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: black; 
}
</style>
""", unsafe_allow_html=True)

st.markdown( '<h1 style ="font-size:50px;color:white;background-color:black;text-align:center;font-family:times new roman;" >Parkinson disease prediction</h1>', unsafe_allow_html=True )

df=pd.read_csv('../data/raw/Heart-Disease-Patients-Records.csv')

box_11, box_12, box_13, box_14 =   st.columns( 4 )

# Row 1

age = box_11.slider( 'age',
          min_value= df['age'].min(),
          max_value= df['age'].max(),key='age_slider')

sex = box_12.selectbox( 'sex',
             options = df['sex'].unique())

cholesterol_level = box_13.slider( 'cholesterol_level',
          min_value= df['cholesterol_level'].min(),
          max_value= df['cholesterol_level'].max(),key='Cholesterol_slider')

chest_pain_type = box_14.selectbox( 'chest_pain_type',
             options = df['chest_pain_type'].unique())

# Row 2

box_21, box_22, box_23, box_24 =   st.columns( 4 )

resisting_blood_pressure= box_21.slider( 'resisting_blood_pressure',
          min_value= df['resisting_blood_pressure'].min(),
          max_value= df['resisting_blood_pressure'].max(),key='blood_pressure_slider')

fasting_blood_sugar=box_22.selectbox('fasting_blood_sugar',
             options = df['fasting_blood_sugar'].unique())

rest_ecg = box_23.selectbox('rest_ecg',
             options = df['rest_ecg'].unique())

max_heart_rate_achieved = box_24.slider( 'max_heart_rate_achieved',
          min_value= df['max_heart_rate_achieved'].min(),
          max_value= df['max_heart_rate_achieved'].max(),key= 'heart_rate')

# Row 3

box_31, box_32, box_33, box_34 =   st.columns( 4 )

exercise_induced_angina= box_31.selectbox( 'exercise_induced_angina',
          options = df['exercise_induced_angina'].unique())

st_depression= box_32.selectbox( 'st_depression',
          options = df['st_depression'].unique())

st_slope=box_33.selectbox( 'st_slope',
          options = df['st_slope'].unique())

num_major_vessels= box_34.slider( 'max_heart_rate_achieved',
          min_value= df['max_heart_rate_achieved'].min(),
          max_value= df['max_heart_rate_achieved'].max(),key='number_of_vessels')

# Row 4

box_41, box_42 =   st.columns( 2 )

thalassemia=box_41.selectbox( 'thalassemia',
          options = df['thalassemia'].unique())

diagnosis=box_42.selectbox( 'diagnosis',
          options = df['diagnosis'].unique())

# Initialize session state
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        'gender', 'sex', 'cholesterol level', 'chest pain type',
        'resisting blood pressure', 'fasting_blood_sugar', 'rest_ecg',
        'max heart rate achieved', 'exercise induced angina', 'st depression', 'st slope','num major vessels'
    ])

# Create row
input_data = pd.DataFrame([{
    'age': age,
    'sex':sex,
    'cholesterol level': cholesterol_level,
    'chest pain type': chest_pain_type,
    'resisting blood pressure': resisting_blood_pressure,
    'fasting blood sugar': fasting_blood_sugar,
    'rest ecg': rest_ecg,
    'max heart rate achieved': max_heart_rate_achieved,
    'exercise induced angina': exercise_induced_angina,
    'st depression': st_depression,
    'st slope': st_slope,
    'num major vessels': num_major_vessels
}])


st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;  /* Green background */
        color: white;               /* White text */
        height: 3em;
        width: 100%;
        border-radius: 10px;
        margin-left:100%;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("Add Data", key="add_data_button"):
        st.session_state.data.loc[len(st.session_state.data)] = input_data.iloc[0]

with col2:
    if st.button("Clear Table", key="clear_data_button"):
        st.session_state.data = st.session_state.data.iloc[0:0]

# Display table
st.dataframe(st.session_state.data)