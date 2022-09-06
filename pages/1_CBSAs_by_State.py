import pandas as pd
import streamlit as st

df = pd.read_csv('cbsa.csv')

title = st.text_input(label='Enter State',value='OH')
st.write(df.loc[df['state_id'] == title,'cbsa_name'])
