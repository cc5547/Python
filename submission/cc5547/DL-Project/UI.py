import streamlit as st
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

def user_interface():
    st.title("뼈대 작업 중...")

    container_count = 3
    containers = [st.container() for i in range(container_count)]
    image = ["https://i.imgur.com/t4O7ozH.jpg", "https://i.imgur.com/idnsDBs.gif", "https://i.imgur.com/fvRG1Tj.gif"]

    [st.image(image, width=500) for image in (image_list := [image for image in image_urls])]
    
    # for i in range(container_count):
    #     with containers[i]:
    #         st.image(image[i], width = 500)