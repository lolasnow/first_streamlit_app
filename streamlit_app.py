import streamlit
import pandas
import requests 
import snowflake.connector

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text(' 🥗 Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#Let's only display what they've chosen
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section to display API response 
streamlit.header('Fruityvice Fruit advice !')

#add textbox
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ' + fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# normalize the json response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# show result
streamlit.dataframe(fruityvice_normalized)


#Snowflake connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
