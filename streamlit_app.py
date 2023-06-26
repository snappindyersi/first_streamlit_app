import streamlit
streamlit.title ('My Parents New Healthy Diner')


streamlit.header ('Breakfast Menu')
streamlit.text ('🐔 Chicken')
streamlit.text ('🥑🍞 Avocado Toast')


streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Here will show the pick list code 
streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index))

# display the table on the page

streamlit.dataframe (my_fruit_list)
