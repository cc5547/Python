import streamlit as st
import pandas as pd
import numpy as np

class Sidebar:
    def __init__(self, df) -> None :
        self.sb = st.sidebar
        self.df = df
        self.area = self.df['지사명'].drop_duplicates().tolist()
        self.sb.title('지역을 선택해주세요.')
        self.choice = self.sb.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', self.area, index = 10)
        self.search = self.sb.text_input('상세 검색 (시, 교명등의 키워드를 입력 :smile:)', value = '')

    def function_sidebar(self):
        for i in range(len(self.area)) : 
            if self.choice == self.area[i] : 
                result = self.df[self.df['지사명'] == self.area[i]]
                
        result = self.df[(self.df['지사명'] == self.choice) & (self.df['시험장소'].str.contains(self.search))]
        result.index = np.arange(1, len(result) + 1)

        return result

    def get_sidebar(self):
        return self.function_sidebar()