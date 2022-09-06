# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:17:46 2022

@author: Zach
"""

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CBSAs",
    page_icon="",
)


file = pd.read_csv('cbsa.csv')

states = file['state_id']
msa = file['cbsa_name']
county = file['county_name']
city = file['city']
zipc = file['zip']



sta_msa = pd.concat([states,msa],axis=1)
state = 'OH'

df = sta_msa.loc[sta_msa['state_id']==state,'cbsa_name']
df = df.drop_duplicates()

print(df)

inputForm = st.form("State Input")
inputState = inputForm.text_input(label='Enter State',value='OH')
inputState = inputState.upper()
submit_button = inputForm.form_submit_button("All Details")
cbsa_button = inputForm.form_submit_button('CBSAs')
cnty_button = inputForm.form_submit_button('Counties')
city_button = inputForm.form_submit_button('Cities')

if submit_button:
    df = sta_msa.loc[sta_msa['state_id']==inputState,'cbsa_name']
    df2 = file.loc[file['state_id'] == inputState,'county_name']
    df3 = file.loc[file['state_id'] == inputState,'city']
    df4 = file.loc[file['state_id'] == inputState,'zip']
    fdf = pd.concat([df,df2,df3,df4],axis=1)
    st.write(fdf)
if cbsa_button:
    df = sta_msa.loc[sta_msa['state_id']==inputState,'cbsa_name']
    df = df.drop_duplicates()
    st.write(df)
if cnty_button:
    df2 = file.loc[file['state_id'] == inputState,'county_name']
    df2 = df2.drop_duplicates()
    st.write(df2)
if city_button:
     df3 = file.loc[file['state_id'] == inputState,'city']
     df4 = file.loc[file['state_id'] == inputState,'zip']
     fdf = pd.concat([df3,df4],axis=1)
     # fdf = fdf.drop_duplicates()
     st.write(fdf)
 

    


    
