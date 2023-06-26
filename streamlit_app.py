import streamlit
streamlit.title ('My Parents New Healthy Diner')


streamlit.header ('Breakfast Menu')
streamlit.text ('🐔 Chicken')
streamlit.text ('🥑🍞 Avocado Toast')


streamlit.header ('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Here will show the pick list code 
fruit_selected = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]

# display the table on the page

streamlit.dataframe (fruits_to_show)
