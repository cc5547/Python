# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    "두번째 시작"
)

guess = st.slider('번호를 고르세요', min_value=1, max_value=10, step=1)
print(f" 당신이 선택한 번호는 {guess} 입니다.")
st.write(f" 당신이 선택한 번호는 {guess} 입니다.")
prize = st.slider('당첨 상금을 지정해주세요', min_value=10000, max_value=10000000, step=5000)
print(f" 당첨금액은  {prize} 입니다.")


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )