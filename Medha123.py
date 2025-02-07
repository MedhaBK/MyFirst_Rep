import numpy as np
import pandas as pd
import streamlit as st

st.title("Hello People!, Medha here!!!")
st.title("Welcome Everyone we are learning Python <3 :)")
st.write("Pyhton requires practice")
data = pd.DataFrame({'c1': [23, 45, 67, 89],'c2': ['A','B','C','D']})

st.write("Below is the table for data: ")
st.write(data)

chart_data = pd.DataFrame(np.random.randn(20,3), columns= ['A','B','C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
