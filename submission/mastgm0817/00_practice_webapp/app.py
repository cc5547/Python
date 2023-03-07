import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv("국비지원반.CSV")
df.plot()