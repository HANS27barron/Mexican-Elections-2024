import streamlit as st
import pandas as pd

st.title("Profile")

table = pd.DataFrame(
    [
       {"book": "dune", "rating": 10, "accept?": False},
       {"book": "dune messiah", "rating": 7.5, "accept?": False},
       {"book": "children of dune", "rating": 8.5, "accept?": False},
   ]
)
edited_table = st.data_editor(table, num_rows="dynamic")

favorite_command = edited_table.loc[edited_table["rating"].idxmax()]["book"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")