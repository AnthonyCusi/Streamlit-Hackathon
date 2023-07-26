import streamlit as st
import connection
import pandas as pd

st.set_page_config (layout="wide")
st.title('Supabase Connection Demonstration')
st.write("A 'supa-basic' demonstration of extending Streamlit's ExperimentalBaseConnection to establish a Supabase connection.")

# Explanation and demonstration of usage
st.subheader("Usage")
st.write("1. Create the connection object")
with st.echo():
    conn = st.experimental_connection("supabase", type = connection.SupabaseConnection)
st.write("2. Use object to query database; the data is then pulled from a custom Supabase database!")
with st.echo():
    all_rows = conn.query()
st.table(all_rows)

# Demonstration of pulling specific columns
st.subheader("Filtering")
st.write("Try selecting a specific column to be pulled:")
with st.echo():
    column_filter = st.selectbox("Select a column to view", ["make", "model", "price"])
    select_rows = conn.query(column_filter)
st.table(select_rows)
st.write("Instead of the dropdown, you can also directly input the column name as well.")

