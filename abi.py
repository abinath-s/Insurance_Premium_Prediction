# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#!pip install -U scikit-learn

#!pip install joblib

import streamlit as st
import joblib
import pandas as pd

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Insurance Premium Prediction</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    

    model = joblib.load('model_jobliob_gr')
    p1 = st.slider("Enter Your Age",18,100)
    p1 = str(p1)
    p2=st.selectbox("Sex",("male","female"))


    p3 =st.number_input("Enter Your BMI Value")
    p3 = str(p3)
    p4 = st.slider("Enter Number of Children",0,4) 
    p4 = str(p4)
    
    p5=st.selectbox("Smoker",("yes","no"))

        
    p6 = st.selectbox("Enter Your Region",('northeast','southeast','southwest','northwest'))
    
    if st.button('Predict'):
        df = [[p1,p2,p3,p4,p5,p6]]
        df = pd.DataFrame(df,columns = ['age','sex', 'bmi', 'children', 'smoker','region'])
        prediction = model.predict(df)
        st.success('Insurance Amount is {} '.format(round(prediction[0],2))) 
        
    
    
    
    
if __name__ == '__main__':
    main()
    
    