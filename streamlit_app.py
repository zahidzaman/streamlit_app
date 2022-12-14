import pandas, streamlit

streamlit.title('Healthy Dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('Omega3 & Blueberry Oatmeal')	
streamlit.text('Kale, Spinach & Rocket Smoothie')	
streamlit.text('Hard-Boiled Free-Range Egg')	
streamlit.header('Build Your Own Smoothie')	

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
selected_fruits = streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[selected_fruits]
streamlit.dataframe(fruit_to_show)
