import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0


button = st.button("inc value")

if button:
    st.session_state.counter += 1

st.header(st.session_state.counter)    