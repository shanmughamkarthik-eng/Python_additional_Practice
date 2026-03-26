import streamlit as st

st.title("Step 1: The Counter")

if "count" not in st.session_state:
    st.session_state.count = 0

st.header(f"current count: {st.session_state.count}")

if st.button("increment ++"):
    st.session_state.count += 1
    st.rerun()

if st.button("decrement --"):
    st.session_state.count -= 1
    st.rerun()

if st.button("Reset"):
    st.session_state.count = 0
    st.rerun()

