import streamlit as st
import pandas as pd

st.title("My Mom's New Healthy Dinner")

st.header('Breakfast Favorites')
st.text(' 🥣 Omega 3 & Blueberry Oatmeal')
st.text(' 🥗 Kale, Spinach and Rocket Smoothie')
st.text(' 🐔 Hard-Boiled Free-Range Egg')
st.text(' 🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_options = list(my_fruit_list.index)
fruits_selected = st.multiselect("Pick some fruits:", fruits_options, ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
st.dataframe(fruits_to_show)

