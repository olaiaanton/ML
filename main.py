# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:49:49 2022

@author: Usuario
"""

import streamlit as st 

st.title("MY FIRST ML APP")

my_text = st.text("Some text")

my_button = st.button("Run ML computation")

if my_button:
    st.title("SOS")
    
hungry = st.checkbox("I am hungry")

if hungry:
    st.write("Go eat")