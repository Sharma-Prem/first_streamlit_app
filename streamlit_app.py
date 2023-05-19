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
st.write("Loaded fruit list:", my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include
fruits_options = list(my_fruit_list.set_index('Fruit'))
st.write("Options:", fruits_options)

default_fruits = ['Avocado', 'Strawberries']
fruits_selected = st.multiselect("Pick some fruits:", fruits_options, default=default_fruits)
st.write("Selected fruits:", fruits_selected)

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
st.dataframe(fruits_to_show)


