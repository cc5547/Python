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
        st.title(‘Streamlit Tutorial’)
        ## Header/Subheader
        st.header(‘This is header’)
        st.subheader(‘This is subheader’)
        ## Text
        st.text(“Hello Streamlit! 이 글은 튜토리얼 입니다.”)
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
        ## Latex
        st.latex(r”Y = \alpha + \beta X_i”)
        ## Latex-inline
        st.markdown(r”회귀분석에서 잔차식은 다음과 같습니다 $e_i = y_i — \hat{y}_i$”)
    with col4 :




if __name__ == '__main__':
  main()