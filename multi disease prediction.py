# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:37:55 2024

@author: tussh
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
import numpy as np

scaler = StandardScaler()

diabetes_model= pickle.load(open('D:/Multiple Disease detection/Models/diabetes_model.sav','rb'))
heart_model= pickle.load(open('D:/Multiple Disease detection/Models/heart_disease.sav','rb'))
liver_model= pickle.load(open('D:/Multiple Disease detection/Models/Liver_Disease.sav','rb'))

#sidebar for navigation
with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction'],
                          default_index=0)

#Diabetes Prediction Page
if(selected== 'Diabetes Prediction'):
    st.title('Diabetes Prediction')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]
        user_input=np.array(user_input).reshape(1,-1)
        user_input = scaler.fit_transform(user_input)
        
     
        diab_prediction = diabetes_model.predict(user_input)
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    
#Heart Disease Prediction Page
if( selected =='Heart Disease Prediction'):
    st.title('Heart Disease Prediction')
     
    col1, col2, col3 = st.columns(3)
    with col1:
       Age = st.text_input('Age')
    with col2:
       Gender = st.text_input('Gender (Male=1, Female=0)')
    with col3:
       CP = st.text_input('Chest Pain types')
    with col1:
       RestBP = st.text_input('Resting Blood Pressure')
    with col2:
       Chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
       FBS = st.text_input('Fasting Blood Sugar> 120 mg/dl')
    with col1:
       ECG = st.text_input('Resting Electrocardiographic results')
    with col2:
       MaxHR = st.text_input('Maximum Heart Rate achieved')
    with col3:
       Exang = st.text_input('Exercise Induced Angina')
    with col1:
       Oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
       Slope = st.text_input('Slope of the peak exercise ST segment')
  
    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):

       user_input = [Age, Gender, CP, RestBP, Chol, FBS, ECG, MaxHR, Exang, Oldpeak, Slope]
       
       user_input = [float(x) for x in user_input]

       heart_prediction = heart_model.predict([user_input])

       if heart_prediction[0] == 1:
           heart_diagnosis = 'The person is having heart disease'
       else:
           heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

    
if (selected=='Liver Disease Prediction'):
    st.title('Liver Disease Prediction')
    
    col1, col2, col3 = st.columns(3)

    with col1:
       Age = st.text_input('Age')
    with col2:
       Gender = st.text_input('Gender')
    with col3:
       Tblb = st.text_input('Total Bilirubin')
    with col1:
       Dblb = st.text_input('Direct Bilirubin')
    with col2:
       Alk = st.text_input(' Alkphos Alkaline Phosphotase')
    with col3:
       SGPT = st.text_input(' SGPT Alamine Aminotransferase')
    with col1:
       SGOT = st.text_input('SGOT Aspartate Aminotransferase')
    with col2:
       Protien = st.text_input('Total Protiens')
    with col3:
       ALB = st.text_input(' ALB Albumin')
    with col1:
       AGR = st.text_input('A/G Ratio Albumin and Globulin Ratio')


   # code for Prediction
    liver_diagnosis = ''

   # creating a button for Prediction    
    if st.button("Liver Disease Prediction"):

       user_input = [Age,Gender,Tblb,Dblb,Alk,SGPT,SGOT,Protien,ALB,AGR]
       
       user_input = [float(x) for x in user_input]
       user_input=np.array(user_input).reshape(1,-1)
       user_input = scaler.fit_transform(user_input)
       
       liver_prediction = liver_model.predict(user_input)

       if liver_prediction == 1:
           liver_diagnosis = "The person has Liver disease"
       else:
           liver_diagnosis = "The person does not have Liver disease"

    st.success(liver_diagnosis)
    
