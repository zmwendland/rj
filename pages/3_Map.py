# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 07:11:00 2022

@author: Zach
"""


import pandas as pd
import streamlit as st
 
df = pd.read_csv('map.csv')



inputForm = st.form("State Input")
inputState = inputForm.text_input(label='Enter State',value='OH')
inputState = inputState.upper()
submit_button = inputForm.form_submit_button("All Details")
if submit_button:
    df1 = df.loc[df['state_id']==inputState,'lat']
    df2 = df.loc[df['state_id']==inputState,'lon']
    df3 = df.loc[df['state_id']==inputState,'cbsa_name']
    fdf = pd.concat([df1,df2,df3],axis=1)
    fdf = fdf.drop_duplicates()
    st.map(fdf)

