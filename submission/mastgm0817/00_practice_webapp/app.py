import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("submission/mastgm0817/00_practice_webapp/국비지원반.CSV")
df.plot()