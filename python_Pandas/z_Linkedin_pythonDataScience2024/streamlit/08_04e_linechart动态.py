import time
import numpy as np 
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt 

rows = np.random.randn(1,1)

'Growing Line Chart:'
chart = st.line_chart(rows)

for i in range(1, 100):
  new_rows = rows[0] + np.random.randn(1,1) # rows[0] is the first element of the array rows
  chart.add_rows(new_rows)
  rows= new_rows
  time.sleep(0.05) # 0.05 seconds

'Terminal执行指令: streamlit run 08_04e.py'


values = np.random.rand(10) # 10 random numbers between 0 and 1 == length to be 10 data points
'matplotlibs Line Chart:'
fig, ax = plt.subplots() # fig, ax = plt.subplots() is equivalent to fig = plt.figure() and ax = fig.add_subplot(111)
ax.plot(values)
st.pyplot(fig)







