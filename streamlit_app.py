import streamlit
import pandas

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# lets put a pick list here so they can pick fruit they want to include.
streamlit.multiselect( "Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

#Display table on the page
streamlit.dataframe(my_fruit_list)


