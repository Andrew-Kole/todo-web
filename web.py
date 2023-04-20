import streamlit as st
import modules.functions as func

todos = func.get_todos()

st.title("My to-do app")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new to-do...")