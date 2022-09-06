
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 07:11:00 2022

@author: Zach
"""


import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

df = pd.read_csv('map.csv')

inputForm = st.form("State Input")
inputState = inputForm.text_input(label='Enter State',value='OH')
inputState = inputState.upper()
submit_button = inputForm.form_submit_button("All Details")

st.map(df)
