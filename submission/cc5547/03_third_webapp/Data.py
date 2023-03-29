import pandas as pd
import joblib
import streamlit as st
# @st.cache

# data 생성
class CreateData:
    def __init__(self) -> None:
        self.jobs = "submission/cc5547/03_third_webapp/xgb_model.joblib"

    # read / df 전처리 해줄 거 작성 하기
    def load_df(self):
        try : 
            data = joblib.load(self.jobs)
            return data
        except Exception as e : 
            return st.error(e)
        
    # 메인에서 호출 한번에 처리할 것 
    def create_data(self) :  
        return self.load_df()