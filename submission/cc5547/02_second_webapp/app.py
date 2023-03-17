import requests
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np

# 중앙 정렬
  st.set_page_config(layout="wide") 
  # 8:2 비율의 컬럼 생성
  col1, col2 = st.columns([8, 2])
  # 탭 생성 : 첫번째 탭의 이름은 Tab_1로, Tab_2로 표시
  tab1, tab2= st.tabs(['필기 년도 별 합격률' , '응시자 및 합격자 수'])

# 데이터 프레임 생성
def create_df():
  df_URL = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EC%8B%9C%ED%97%98%EC%9E%A5%EC%86%8C_%EA%B0%80%EA%B3%B5%EC%B2%98%EB%A6%AC.csv"
  # df_URL_g_1 = "https://raw.githubusercontent.com/cc5547/Python/main/submission/cc5547/02_second_webapp/%EA%B7%B8%EB%9E%98%ED%94%84_1.csv"
  
  df = pd.read_csv(df_URL).iloc[:, 1:]
  # df_g_1 = pd.read_csv(df_URL_g_1)
  df.index += 1
  
  return df

# 사이드바
def side_bar(df) :
  s_bar = st.sidebar
  s_bar.title('지역을 선택해주세요.')
  area = df['지사명'].drop_duplicates().tolist()
  choice = s_bar.selectbox('지역 선택(재검색시 상세 검색을 지워 주세요)', area, index = 10)

  for i in range(len(area)):
    if choice == area[i]: 
      result = df[df['지사명'] == area[i]]
    else : pass 
   
  search = s_bar.text_input('상세 검색 \n (시, 교명등의 키워드를 입력 :smile:)')
  result = df[(df['지사명'] == choice) & (df['시험장소'].str.contains(search))]
  result.index = np.arange(1, len(result) + 1) 

  return df, result

# 그래프 생성
def create_graph(image_url):
  image = Image.open(requests.get(image_url, stream=True).raw)
  return image

def main():
  df, result = side_bar(create_df()) 

  with col1 :
    st.title(':smile: 시험장소를 안내해드립니다 :smile:')
    st.dataframe(result, width=800, height=500)
    st.subheader(":smile: 귀하의 합격을 기원합니다! :smile:")

  with col2 : st.markdown("[![Foo](https://i.imgur.com/SywJPmA.png)](https://map.naver.com/)"

  with tab1 : image_url = "https://i.imgur.com/wOY7lUx.png"
    st.image(create_graph(image_url), use_column_width=True)
    
  with tab2 : image_url = "https://i.imgur.com/C9nrLkC.png"
    st.image(create_graph(image_url), use_column_width=True)
    
if __name__ == '__main__':
  main()