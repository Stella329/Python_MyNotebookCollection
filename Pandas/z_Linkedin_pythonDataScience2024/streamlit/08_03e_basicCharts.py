import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ["column1","column2","column3"]

data = pd.DataFrame(np.random.randint(30, size=(30, 3)),columns=col_names) # random numbers：0-29； size: 30 rows, 3 columns; 

'line graph:'
st.line_chart(data)

'bar graph:'
st.bar_chart(data)


# Streamlit is not able to display pie chart; using matplotlib instead
'create a dataset：'
animals = ['cat', 'cow', 'dog']
heights  = [30, 150, 80] # in cm

'pie chart:'
fig, ax = plt.subplots()
ax.pie(heights,labels=animals)

st.pyplot(fig) # st.pyplot(fig) is equivalent to plt.show()

# This code will display a pie chart in Streamlit, showing the distribution of heights for the animals. 
# While Streamlit does not have a built-in function for scatter plots, you can use other Python visualization libraries like Matplotlib to create and display them within Streamlit.