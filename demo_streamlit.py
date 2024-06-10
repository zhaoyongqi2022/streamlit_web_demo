import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and description
st.title("Streamlit Demo App")
st.write("This is a simple demonstration of a Streamlit app.")

# Sidebar with user input
st.sidebar.header("User Input")
user_name = st.sidebar.text_input("What's your name?")
user_number = st.sidebar.slider("Pick a number", 1, 100, 50)

# Display user input
st.write(f"Hello, {user_name}! You picked number {user_number}.")

# Generate a random dataframe
st.header("Random Data")
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

# Display the dataframe
st.write("Here is a random dataframe:")
st.dataframe(data)

# Plot the data
st.header("Data Visualization")
st.write("A simple line chart of the dataframe columns:")
st.line_chart(data)

# Matplotlib chart
st.write("A histogram of the first column using Matplotlib:")
fig, ax = plt.subplots()
ax.hist(data['A'], bins=15)
st.pyplot(fig)

# User-uploaded file
st.header("File Upload")
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file is not None:
    uploaded_data = pd.read_csv(uploaded_file)
    st.write("Here is the data you uploaded:")
    st.dataframe(uploaded_data)

# Ending note
st.write("Thank you for using this demo app!")
