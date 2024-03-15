# Import Streamlit
import streamlit as st

# Display a header
st.header("Hello, Streamlit!")

# Create a button
if st.button("Say hello"):
    # Display a message when the button is clicked
    st.write("Hello there! Nice to see you :)")
