import pandas, streamlit

streamlit.title('Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega3 & Blueberry Oatmeal')	
streamlit.text('Kale, Spinach & Rocket Smoothie')	
streamlit.text('Hard-Boiled Free-Range Egg')	
streamlit.header('Build Your Own Smoothie')	

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
