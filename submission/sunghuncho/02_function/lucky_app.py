# streamlit 라이브러리 호출
# 상대경로 복사 : submission/qus0in/02_function/app.py
import streamlit as st
import random

# st.write("함수를 응용해서 페이지 만들어보기")

st.write("# 행운 뽑기")

# 0~9까지의 번호를 고르면

number = st.selectbox("번호를 골라주세요", list(range(10)))
st.write(f"내가 고른 번호 : {number}")

# 상금 -> 상금을 내가 입력하게 함

# prize = st.number_input(
#   "당첨 시의 상금을 입력해주세요",
#   min_value=1000,
#   max_value=10000
# )
prize = st.slider(
  "당첨 시의 상금을 입력해주세요",
  1000,
  10000,
  step=100,
)
st.write(f"당첨 시의 상금 : {prize}")

def my_fun():
  # random.choice? -> 추첨 로직
  st.balloons()

# button -> 당첨입니다! / 떨어졌습니다
pushed = st.button("당첨 알아보기", on_click=my_fun)

if pushed:
  # st.write("버튼이 눌렸습니다")
  result = random.choice(range(10))
  st.info(f"뽑힌 번호는... {result}번!")
  if result == number:
    st.success(f"축하합니다! 당첨입니다. 상금 {prize}원을 받으세요!")
  else:
    st.error(f"아쉽습니다! 낙첨입니다. 상금 {prize}원은 없던일로 ㅠㅠ")
