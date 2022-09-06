# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 21:55:22 2022

@author: Zach
"""

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
# import 

height = st.sidebar.slider("Height", 200, 2000, 300, 100)
width = st.sidebar.slider("Width", 200, 2000, 600, 100)

components.html("""
                   <iframe title="RJ_CBSA - Overview" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMTFkMDNmZWQtMTQzNi00N2RmLTk0MTctM2IwZGNkMTYzZmExIiwidCI6Ijc5NmMxMTY3LTRjNTEtNDkxZC05MDhjLWZiNmJjMThiMDIyZiJ9" frameborder="0" allowFullScreen="true"></iframe>
                   """,height=height,width=width)

