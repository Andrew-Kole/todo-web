import streamlit as st
import modules.functions as func

todos = func.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    func.write_todos(todos)


st.title("My to-do app")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key="new_todo")