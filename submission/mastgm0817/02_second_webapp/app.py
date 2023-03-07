# streamlit 라이브러리 호출
import streamlit as st
import time
import random

def timer_fun():
    with st.spinner('Wait for it...'):
        time.sleep(3)

guess = st.slider('번호를 고르세요', min_value=1, max_value=10, step=1)
print(f" 당신이 선택한 번호는 {guess} 입니다.")
st.write(f" 당신이 선택한 번호는 {guess} 입니다.")
prize = st.slider('당첨 상금을 지정해주세요', min_value=10000, max_value=10000000, step=5000)
st.write(f" 당첨금액은  {prize}원 입니다.")

with st.container():
    pushed = st.button("번호 추첨", on_click=timer_fun)

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

if pushed:
    random_num = random.randint(1,10)
    st.write(f"{random_num}")
    if random_num == guess:
        # st.write(f"당첨")
        st.markdown("<h1 style='text-align: center; color: grey;'>당첨</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: black;'>당첨번호는 :[random_num]</h2>", unsafe_allow_html=True)
        st.write(f"{random_num}")
    else:
        st.markdown("<h1 style='text-align: center; color: grey;'>낙첨</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: black;'>당첨번호는</h2>", unsafe_allow_html=True)
        st.write(f"{random_num}")

