# +
#conda create -n env_name python=3.8
#conda activate env_name
#pip install streamlit
#streamlit run C:\Users\mirya\OneDrive\Documentos\MASTER_BIG_DATA\Vodafone_Elena_Abril\test.py
# -

# First, we will do the imports required for all the process
import altair as alt
import math
import os
import pandas as pd
import streamlit as st

# The first set of elements to test are the text elements, that will allow us to show pieces of text
# and create different parts in our appplication with the titles and headers
st.text("Hello Antonio Y CIA")
st.title("Prueba")
st.header("Streamlit")
st.subheader("Esto es una cabecera.")
st.markdown("Text with *markdown* **format**")  # markdown is very useful to format text elements
