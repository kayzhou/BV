import streamlit as st
import pandas as pd

# Day 1
st.write('今天是研究生一年级下学期第13周的周三！')


# Day 2
st.write('Hello world!')


# Day 3
st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
     
     
# Day 4

# Day 5
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# 样例 1
st.write('Hello, *World!* :sunglasses:')

# 样例 2
st.write(1234)

# 样例 3
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# 样例 4
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# 样例 5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


# Day 6
# Day 7
# Day 8
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# 样例 1
st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 样例 2
st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3
st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# 样例 4
st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)


# Day 9
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# Day 10
st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)


# Day 11
import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)


# Day 12
st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")
     
     
# Day 13
# Day 14
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('`streamlit_pandas_profiling`')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

pr = df.profile_report()
st_profile_report(pr)


# Day 15
st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


# Day 16
# Day 17
# Day 18
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
     df = pd.read_csv(uploaded_file)
     st.subheader('DataFrame')
     st.write(df)
     st.subheader('Descriptive Statistics')
     st.write(df.describe())
else:
     st.info('☝️ Upload a CSV file')

# Day 19
# Day 20
# Day 21
# Day 22
# Day 23
# Day 24
# Day 25
# Day 26
# Day 27
# Day 28
# Day 29
# Day 30
