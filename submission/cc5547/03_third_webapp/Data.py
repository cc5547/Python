import pandas as pd
import joblib
import streamlit as st
# @st.cache
# df 생성
class CreateData:
    # df URL
    def __init__(self) -> None:
        self.jobs = "submission/cc5547/03_third_webapp/xgb_model.joblib"

    # read / df 전처리 해줄 거 작성 하기
    def load_df(self):
        try:
            data = joblib.load(self.jobs)
        except Exception as e:
            return st.error(e)
        return data
        
    # 메인에서 호출 한번에 처리할 것 
    def create_data(self) : 
        data = dself.load_df()
        return data