import streamlit as st
from SideBar import Sidebar
from Data import Create
st.set_page_config(page_title="마싯는 머신러닝", layout="wide")

def user_interface():
    df, df_g1, df_g2 = Create().get_data()
  
    col1, col2 = st.columns([8, 2])
    with col1 : 
        st.title(":smile: 시험장소를 안내해드립니다 :smile:")
        st.dataframe(Sidebar(df).get_sidebar(), width=1000, height=500)
        st.subheader(":smile: 귀하의 합격을 기원합니다! :smile:")
    with col2 : 
        st.markdown("[![Foo](https://i.imgur.com/SywJPmA.png)](https://map.naver.com/)")

    tab1, tab2 = st.tabs(['필기 년도 별 합격률' , '응시자 및 합격자 수'])
    with tab1 : st.plotly_chart(create_graph(df_g1, None))
    with tab2 : st.plotly_chart(create_graph(None, df_g2))