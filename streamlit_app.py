import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# lets put a pick list here so they can pick fruit they want to include.
fruits_selected = streamlit.multiselect( "Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show =  my_fruit_list.loc[fruits_selected]

#Display table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
     return fruityvice_normalized

#New Section to display fruityvice 
streamlit.header('Fruiyvice Fruit Advice')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
      streamlit.error("PLEASE SELECT A FRUIT INFORMATION")
    else:
         back_from_function = get_fruityvice_data(fruit_choice)
         streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()
    
#s#treamlit.text(fruityvice_response.json())
# Dont run anything psdt here while we troubleshoot
streamlit.stop()

streamlit.header( THE FRUIT LOAD LIST COMTAINS:")
# Snowflake functions related 
                 
def get_fruit_load_list():
    with  my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.my_cur.fetchall()
                 
# Add Button to load the fruit 
if streamlit.button('GEt Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

#Second text box
add_my_fruit = streamlit.text_input('What fruit would you like ADD ', 'banana')
streamlit.write('The user entered INTO NEW', add_my_fruit)

streamlit.write('THANKS FOR ADDING ', add_my_fruit)
my_cur.execute("Insert into fruit_load_list values ('from streamlit')")



