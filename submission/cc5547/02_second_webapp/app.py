import streamlit as st
import pandas as pd
import numpy as np
# 중앙 정렬
st.set_page_config(layout="wide") 
# 단일 컬럼 생성
col = st.columns(1)[0]
# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab_1' , 'Tab_2'])


# 데이터 프레임 생
def create_df():
  # DF_URL
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  # df언네임 삭제
  df = pd.read_csv(df_URL).iloc[:, 1:]
  # df인덱스 올림       
  df.index += 1
  # df 반환
  return df  

# 사이드바
def side_bar() :
  # 사이드바 생성 : 사이드 바를 s_bar 로 생성.
  s_bar = st.sidebar
  # df 생성 및 함수 호출
  df = create_df()
  # 지역 선택 멘트 타이틀
  s_bar.title('지역을 선택해주세요.')
  # area에 df에서 열 중에서 지사명인 열에 값들을 중복을 제거하고 리스트로 변환
  area = df['지사명'].drop_duplicates().tolist()
  # choice라는 변수에 셀렉트박스의 값에서 선택된 값들을 저장
  choice = s_bar.selectbox('지역 선택', area)
  # 위 area 리스트의 크기 만큼 반복 그냥 if문을 area의 리스트 크기만큼 작성
  for i in range(len(area)):
    if choice == area[i]: # 초이스 셀렉트바에서 선택한 값이 area의 인덱스 값과 일치한다면
      result = df[df['지사명'] == area[i]] # result에 지사명이 지역을 선택한 값들의 데이터들은 저장
      result.index = np.arange(1, len(result) + 1) # result 데이터프레임의 인덱스를 1부터 시작하도록 변경
  return df, result # 데이터프레임과 지역선택의 값을 return 
  
def main():
  df, result = side_bar()
  with col :
    # column 에 담을 내용
    st.title('안녕하세요 시험장소를 안내해드립니다. :울음')
    st.dataframe(result.style.set_properties(**{'text-align': 'center'}), width=1000, height=500)
  with tab1 :
    # tab1 에 담을 내용
    pass
  with tab2 :
    # tab2 에 담을 내용
    pass
if __name__ == '__main__':
  main()