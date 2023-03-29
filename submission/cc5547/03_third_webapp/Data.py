import pandas as pd
import joblib
import streamlit as st
# @st.cache

# data 생성
class CreateData:
    def __init__(self) -> None :
        self.jobs = "submission/cc5547/03_third_webapp/xgb_model.joblib"

    # read 전처리 해줄 거 작성 하기
    def create_data(self) :
        try : 
            return joblib.load(self.jobs)
        except Exception as e : 
            return st.error(e)
        
    # handle에서 호출 / 한번에 처리할 것 
    def result_data(self) : 
        return self.create_data()