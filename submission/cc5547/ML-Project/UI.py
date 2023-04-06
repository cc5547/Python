import streamlit as st
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

def user_interface():
    st.title("뼈대 작업 중...")
    col1, col2 = st.columns([5, 5])
    with col1 :
        st.image("https://i.imgur.com/fvRG1Tj.gif", width = 500)
    with col2 :
        st.image("https://i.imgur.com/idnsDBs.gif", width = 500)

    # containers = [st.container() for i in range(3)]

    # with containers[0]:
    #     st.title("뼈대 작업 중...")
        
    # with containers[1]:
    #     st.image("https://i.imgur.com/idnsDBs.gif", width = 500)

    # with containers[2]:
    #     st.image("https://i.imgur.com/fvRG1Tj.gif", width = 500)