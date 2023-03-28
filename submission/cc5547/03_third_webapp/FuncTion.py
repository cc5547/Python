import streamlit as st
import numpy as np
import pandas as pd

class Function:
    def __init__(self, data, blood, hbit, gender, heart, age) -> None:
        self.data = data
        self.ment_str = "여기가 머신러닝 시각화_"

    def into_xgb_model(self):
        return self.ment_str

    def create_model(self):
        result = self.into_xgb_model()
        return result