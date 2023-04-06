import streamlit as st
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

def user_interface():
    st.title("뼈대 작업 중...")

    container_count = 3
    containers = [st.container() for i in range(container_count)]
    with containers[0]:
        st.image("https://i.imgur.com/t4O7ozH.jpg", width = 500)
        
    with containers[1]:
        st.image("https://i.imgur.com/idnsDBs.gif", width = 500)

    with containers[2]:
        st.image("https://i.imgur.com/fvRG1Tj.gif", width = 500)