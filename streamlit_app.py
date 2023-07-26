import streamlit as st
import connection
import pandas as pd

st.set_page_config (layout="wide")
st.title('Supabase Connection Demonstration')
st.text("This is a demonstration of extending Streamlit's ExperimentalBaseConnection to establish a Supabase connection.")

# Initializing connection and connection object
conn = st.experimental_connection("supabase", type = connection.SupabaseConnection)
c = conn.cursor()

# Demonstration of pulling data
st.text("The connection object is then used to pull data from a custom database!")
all_rows = conn.query()
st.table(all_rows.data)

# Demonstration of pulling specific columns
st.text("Try selecting a specific column to be pulled from the Supabase database:")
column_filter = st.selectbox("Select a column to view", ["make", "model"])
select_rows = conn.query(column_filter)
st.table(select_rows.data)