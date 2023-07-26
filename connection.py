from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import streamlit as st
import supabase
import pandas as pd

class SupabaseConnection(ExperimentalBaseConnection[supabase.create_client]):
    '''Connection implementation for Supabase'''

    db = None

    def _connect(_self, **kwargs) -> supabase.create_client:
        # Gets database to use; otherwise uses custom 'vehicles' database
        if "database" in kwargs:
            SupabaseConnection.db = kwargs.pop("database")
        else:
            SupabaseConnection.db = st.secrets["supabase_database"]
        # Establishes connection
        url = st.secrets["supabase_url"]
        key = st.secrets["supabase_key"]
        return supabase.create_client(url, key)

    def cursor(self) -> supabase.create_client:
        return self._instance.table(SupabaseConnection.db)

    def query(self, filter: str = "*", ttl: int = 600, **kwargs) -> pd.DataFrame:
        @cache_data(ttl = ttl)
        def _query(filter: str = "*") -> pd.DataFrame:
            cursor = self.cursor()
            data_table = cursor.select(filter).execute()
            return pd.DataFrame(data_table.data)
        
        return _query(filter, **kwargs)       
