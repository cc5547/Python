import streamlit as st
from PIL import Image
import requests
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def create_df() :
    pass

def create_graph() :
    pass

def main() :
    col1, col2 = ([8,2])
    with col1 :
        ## Title
        st.title("treamlit Tutorial")
        ## Header/Subheader
        st.header("This is header")
        st.subheader("This is subheader")
        ## Text
        st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")
    with col2 :
        ## Markdown syntax
        st.markdown("# This is a Markdown title")
        st.markdown("## This is a Markdown header")
        st.markdown("### This is a Markdown subheader")
        st.markdown("- item 1\n"
                    "   - item 1.1\n"
                    "   - item 1.2\n"
                    "- item 2\n"
                    "- item 3")
        st.markdown("1. item 1\n"
                    "   1. item 1.1\n"
                    "   2. item 1.2\n"
                    "2. item 2\n"
                    "3. item 3")
    with col3 : 
       ## Checkbox
        if st.checkbox(“Show/Hide”):
        st.write(“체크박스가 선택되었습니다.”)
    with col4 :
        ## Radio button
        status = st.radio("Select status.", ("Active", "Inactive"))
        if status == "Active":
            st.success("활성화 되었습니다.")
        else:
            st.warning("비활성화 되었습니다.")

if __name__ == '__main__':
  main()