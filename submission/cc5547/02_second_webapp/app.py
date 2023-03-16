import streamlit as st
import pandas as pd
import numpy as np

def create_set():
  # 중앙 정렬
  st.set_page_config(layout="wide") 
  # 단일 컬럼 생성
  col = st.columns(1)[0]
  # 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
  tab1, tab2= st.tabs(['Tab_1' , 'Tab_2'])
  return col, tab1, tab2

def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  # df언네임 삭제
  df = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림
  df.index += 1
  return df


# 사이드바
def side_bar() :
  s = create_set()
  # 사이드바 생성 : 사이드 바를 s_bar 로 생성.
  s_bar = st.sidebar

  s_bar.title('여기가 사이드바 입니다.\n 지역(특별시, 광역시, 시 ...)')
  area = ['서울특별시', '인천광역시', '경기도']

  choice = s_bar.selectbox('지역 선택', area)

  if choice == area[0] :
    st.write('서울을 선택하셨습니다.')
  elif choice == area[1] :
    st.write('인천광역시를 선택하셨습니다.')
  elif choice == area[2] :
    st.write('경기도를 선택하셨습니다.')
  else : pass
  

def main():
  col, tab1, tab2 = create_set()

  df = create_df()

  side_bar()

  with col :
    # column 에 담을 내용
    st.title('# 프레임 결과')
    st.write(df.head(40), width = 5000)
  
  with tab1 :
    # tab1 에 담을 내용
    pass
  with tab2 :
    # tab2 에 담을 내용
    pass

if __name__ == '__main__':
  main()