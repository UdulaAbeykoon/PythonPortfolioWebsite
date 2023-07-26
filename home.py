import streamlit as st
import pandas #panda is a library used to read CSV library

# TO RUN THE PROGRAM PASTE: streamlit run home.py INTO THE TERMINAL
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")#, width=600

with col2:
    st.title ("Udula Abeykoon")
    content = """
    Wagwan. I am Udula! A highly motivated, high school student with strong academic achievements, strong leadership and
effective communication skills. Excels in both individual and team environments and is known for a
hardworking and self-driven approach to studies and responsibilities """

    st.info(content) #info puts bg colour #write removes bg colour

content2 = """
This is my project showcase! Scroll down to see more!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #ratio for column spacing

df= pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df.iterrows():
        st.header(row["tittle"])
        st.write(row["description"])
#       st.write("[Source Code](INSET LINK)")     That is to make a static link
#       st.write(f"[Source Code]({row['url']})")  That is to make the link dynamic using the data.csv file

with col4:
    for index, row in df.itterows():
        st.header(row["tittle"])
        st.write(row["description"])
        st.image("images/" + row["image"])
