# streamlit 라이브러리 호출
# 상대경로 복사 : submission/qus0in/02_function/app.py
import streamlit as st

# st.write("함수를 응용해서 페이지 만들어보기")

st.write("# 행운 뽑기")

# 0~9까지의 번호를 고르면

number = st.selectbox("번호를 골라주세요", list(range(10)))
st.write(f"내가 고른 번호 : {number}")

# 상금 -> 상금을 내가 입력하게 함
# button -> 당첨입니다! / 떨어졌습니다
