import streamlit as st
import pandas as pd

@st.cache_data()
def load_data():
	return pd.read_csv("01 Spotify.csv")
    

st.set_page_config(layout="wide", page_title="Spotify Songs")

df = load_data()

st.session_state["df_spotify"] = df

# df.set_index('Artist', inplace=True)
df.set_index("Track", inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox("Artista", artists)
df_filtered = df[df["Artist"] == artist]

albuns = df_filtered["Album"].value_counts().index 
album = st.selectbox("Album", albuns)

df_filtered_albuns = df[df["Album"] == album]

col1, col2 = st.columns(2)


col1.bar_chart(df_filtered_albuns["Stream"])
col2.line_chart(df_filtered_albuns['Danceability'])
    # st.bar_chart(df_filtered_albuns["Stream"])
    # st.bar_chart(df_filtered["Stream"])
# st.bar_chart(df[df["Stream"] > 1000000000]["Stream"])
