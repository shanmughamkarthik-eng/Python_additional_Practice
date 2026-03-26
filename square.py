import streamlit as st

st.title("The Square Calculator")

number = st.number_input("Enter a number to square:", value = 0.0, step = 1.0)
result = None
if st.button("Calculate Square"):
    result = number * number
    st.success(f"The square of {number} is : {result}")