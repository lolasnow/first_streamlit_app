import streamlit
import pandas

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 & blueberry oatmeal')
streamlit.text(' 🥗 Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard-boiled Free-range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)
